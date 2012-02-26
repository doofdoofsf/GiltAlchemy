#GiltAlchemy
GiltAlchemy is a set of SQLAlchemy models for persisting data returned from the GiltAPI. It will create your database tables.  The models are based on those returned by PyGilt (https://github.com/doofdoofsf/PyGilt)

##Documentation
No doc sorry

##Testing
You'll find some unit tests in the test directory

##Setup
If you want to use it, you'll need a database, SQLAlchemy and PyGilt.

You can install GiltAlchemy as follows:

   `$ sudo python setup.py install`

I tested this on debian using packages `SQLAlchemy, mysql-server, python-mysqldb`

##An example

If you wanted to persist all the products in mens sales, you could do the following (error handling removed for clarity):

```   
   engine = create_engine('mysql://john:john@localhost/giltalchemy')
   Session = sessionmaker(bind=engine)
   session = Session()
   api_key = getenv("GILTAPIKEY")
   giltClient = GiltClient(api_key)
   giltAlchemy = GiltAlchemy()
   
   giltAlchemy.create_all_tables(engine)

   active_sales = giltClient.active("men")
   for sale in active_sales:
    product_urls = sale.product_urls
    for product_url in product_urls:
       product = giltClient.product_detail(product_url)
       self.session.add(product)
       self.session.commit()
```
