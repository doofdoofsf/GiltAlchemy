from PyGilt.GiltClient import GiltClient
from PyGilt.Sale import Sale
from PyGilt.Product import Product
from PyGilt.Image import Image
from PyGilt.SKU import SKU
from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, DateTime, create_engine, BigInteger, Unicode, Integer
from sqlalchemy.orm import sessionmaker, relationship, mapper, clear_mappers

from sqlalchemy.orm import mapper
import sys

class GiltAlchemy():
   def __init__(self):
      """
      bind the GiltAlchemy tables to the PyGilt objects
      """
      self.metadata = MetaData()

      sale    = Table('sale', self.metadata,
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

      product = Table('product', self.metadata,
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
   
      sku     = Table('sku', self.metadata,
                  Column('id', BigInteger(), primary_key=True),            # unique ID for the SKU
	          Column('inventory_status', Unicode(256)),                # inventory status
	          Column('msrp_price', Unicode(256)),                      # msrp price
	          Column('sale_price', Unicode(256)),                      # sale price
	          Column('shipping_surcharge', Unicode(256)),              # shipping surcharge 
	          Column('product_key', BigInteger(), ForeignKey('product.product_id')),
	          )
   
      image   = Table('image', self.metadata,
                  Column('key', BigInteger, autoincrement=True, primary_key=True),           # key to image
                  Column('url', Unicode(256)),           # permalink to image
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

   def create_all_tables(self, engine):
      """
      create all the tables for GiltAchemy
      """
      self.metadata.create_all(engine)

   def drop_all_tables(self, engine):
      """
      create all the tables for GiltAchemy
      """
      try:
         self.metadata.drop_all(engine)
      except Exception:
         pass

   def clear_mappers(self):
      """
      *only* use for testing resets
      """
      clear_mappers()
