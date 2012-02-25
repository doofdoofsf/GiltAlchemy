import unittest, sys
from PyGilt.GiltClient import GiltClient
from PyGilt.Product import Product
from PyGilt.Sale import Sale
from PyGilt.Image import Image
from PyGilt.SKU import SKU
from GiltAlchemy.gilt_alchemy import GiltAlchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestBasic(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      pass

   def setUp(self):
      self.engine = create_engine('mysql://john:john@localhost/giltalchemy')
      Session = sessionmaker(bind=self.engine)
      self.session = Session()

      api_key = getenv("GILTAPIKEY")
      if api_key == None:
         raise Exception("Set the environment variable GILTAPIKEY to your API key")
      self.giltClient = GiltClient(api_key)
      self.giltAlchemy = GiltAlchemy()

   def reset_schema(self):
      self.giltAlchemy.drop_all_tables(self.engine)
      self.giltAlchemy.create_all_tables(self.engine)

   def test_persist_all_mens_products_for_one_sale(self):
      self.reset_schema()
      self.delete_all_data()
      active_sales = self.giltClient.active("men")
      for sale in active_sales:
         product_urls = sale.product_urls
         for product_url in product_urls:
            product = self.giltClient.product_detail(product_url)
            self.session.add(product)
            self.session.commit()
         # break;


   def delete_all_data(self):
     self.session.query(Product).filter().delete()
     self.session.query(Sale).filter().delete()
     self.session.query(SKU).filter().delete()
     self.session.query(Image).filter().delete()

   def delete_all_data(self):
     self.session.query(Product).filter().delete()
     self.session.query(Sale).filter().delete()
     self.session.query(SKU).filter().delete()
     self.session.query(Image).filter().delete()

   def tearDown(self):
      self.giltAlchemy.clear_mappers()
