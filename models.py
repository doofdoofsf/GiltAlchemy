from PyGilt.GiltClient import GiltClient
from PyGilt.Sale import Sale
from PyGilt.Product import Product
from PyGilt.Image import Image
from PyGilt.SKU import SKU
from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, DateTime, create_engine, BigInteger, Unicode, Integer
from sqlalchemy.orm import sessionmaker, relationship, mapper


from sqlalchemy.orm import mapper

metadata = MetaData()

sale    = Table('sale', metadata,
            # Column('id', BigInteger(), autoincrement=True, primary_key=True),          # numeric key
            Column('name', Unicode(256)),                            # sale name
            Column('description', Unicode(1024)),                    # sale description
            Column('sale', Unicode(256)),                            # sale URL
	    Column('sale_key', Unicode(256), primary_key=True),      # ID for the sale
	    Column('store', Unicode(128)),                           # store key
	    Column('sale_url', Unicode(256)),                        # permalink to sale (website)
	    Column('begins', DateTime(timezone=True)),               # time for beginning of sale
	    Column('ends', DateTime(timezone=True)),                 # time for end of sale
	    )

product = Table('product', metadata,
            Column('name', Unicode(256)),                            # product name
	    Column('product_id', BigInteger(), primary_key=True),    # unique ID for the product
	    Column('brand', Unicode(128)),                           # brand name
	    Column('url', Unicode(256)),                             # permalink to product (website)
            Column('description', Unicode(1024)),                    # product description
            Column('fit_notes', Unicode(256)),                       # fit notes
            Column('material', Unicode(256)),                        # material
            Column('care_instructions', Unicode(256)),               # care_instructions 
            Column('origin', Unicode(256)),                          # origin 
	    # Column('sale_id', Unicode(256), ForeignKey('sale.id')),
	    )

sku     = Table('sku', metadata,
            Column('id', BigInteger(), primary_key=True),            # unique ID for the SKU
	    Column('inventory_status', Unicode(256)),                # inventory status
	    Column('msrp_price', Unicode(256)),                      # msrp price
	    Column('sale_price', Unicode(256)),                      # sale price
	    Column('shipping_surcharge', Unicode(256)),              # shipping surcharge 
	    Column('product_key', BigInteger(), ForeignKey('product.product_id')),
	    )

image   = Table('image', metadata,
            Column('url', Unicode(256), primary_key=True),           # permalink to image
	    Column('width', Unicode(256)),                           # image width 
	    Column('height', Unicode(256)),                          # image height 
	    Column('product_id', BigInteger(), ForeignKey('product.product_id')),
	    Column('sale_key', Unicode(256), ForeignKey('sale.sale_key')),
	    )

# mapper(Sale, sale, properties={'products' : relationship(Product)})
mapper(Sale, sale, properties={'images' : relationship(Image)})
mapper(Product, product, properties={'skus' : relationship(SKU), 'images' : relationship(Image)})
mapper(SKU, sku)
mapper(Image, image)

engine = create_engine('mysql://john:john@localhost/giltalchemy')
Session = sessionmaker(bind=engine)
session = Session()

# create the tables
metadata.create_all(engine)

giltClient = GiltClient("88245a15ecbba00eb06bada5be2f55d7")

active_sales = giltClient.active("men")
# sale=active_sales[0]
for sale in active_sales:
   print "processing sale: %s" % sale.name
   product_urls = sale.product_urls
   product = giltClient.product_detail(product_urls[0])
   sku=product.skus[0]
   product_image=product.images[0]
   
   if sale.images:
      sale_image=sale.images[0]
      print "sale image %s" % sale.image

   session.add(sale)
   session.commit()

   print "adding product: %s" % product.name
   session.add(product)
   session.commit()

# session.add(sku)
# session.commit()

# session.add(image)
# session.commit()




"""
for sale in active_sales:
   print sale.name
   print sale.products
   product_urls = sale.products
   for product_url in product_urls:
      print "product URI is %s" % product_url
      product = giltClient.product_detail(product_url)
      print "product name is %s" % product.name

"""
