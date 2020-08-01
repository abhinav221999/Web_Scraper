# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# STORE THE SCRAPED DATA IN A SQLITE DATABASE
# ------------------------------------------------------------------------------------------------------------------
# import sqlite3
# class QuotetutorialPipeline(object):

#    def __init__(self):
#       self.create_connection()
#        self.create_table()

#    def create_connection(self):
#        self.conn = sqlite3.connect("data.db")
#        self.curr = self.conn.cursor()

#    def create_table(self):
#        self.curr.execute("""DROP TABLE IF EXISTS PG_1_tb""")
#        self.curr.execute("""create table PG_1_tb(
#                              product_name text,
#                              product_seller text,
#                              product_price number,
#                              product_image_link text
#                              )""")

#    def process_item(self, item, spider):
#        self.store_db(item)
#       return item

#    def store_db(self, item):
#        self.curr.execute("""insert into PG_1_tb values (?,?,?,?)""", (
#                             str(item['product_name'][0]),
#                            str(item['product_seller'][0]),
#                             str(item['product_price'][0]),
#                             str(item['product_image_link'][0])
#        ))
#        self.conn.commit()
# ----------------------------------------------------------------------------------------------------------------


# STORE THE SCRAPED DATA IN A MYSQL DATABASE
# ----------------------------------------------------------------------------------------------------------------
# import mysql.connector


# class QuotetutorialPipeline(object):

#    def __init__(self):
#       self.create_connection()
#       self.create_table()

#    def create_connection(self):
#        self.conn = mysql.connector.connect(
#            host = "host_name",        # enter your host
#            user = "user_name",        # enter your user
#            passwd = "password",       # enter the password
#            database = "database_name" # enter the name of your database
#        )
#        self.curr = self.conn.cursor()

#    def create_table(self):
#        self.curr.execute("""DROP TABLE IF EXISTS PG_1_tb""")
#        self.curr.execute("""create table PG_1_tb(
#                              product_name text,
#                              product_seller text,
#                              product_price number,
#                              product_image_link text
#                              )""")

#    def process_item(self, item, spider):
#        self.store_db(item)
#        return item

#    def store_db(self, item):
#        self.curr.execute("""insert into PG_1_tb values (%s,%s,%s,%s)""", (
#                             str(item['product_name'][0]),
#                             str(item['product_seller'][0]),
#                             str(item['product_price'][0]),
#                             str(item['product_image_link'][0])
#        ))
#        self.conn.commit()
# ----------------------------------------------------------------------------------------------------------------


# STORE THE SCRAPED DATA IN A MONGODB DATABASE
# ----------------------------------------------------------------------------------------------------------------
# import pymongo


# class QuotetutorialPipeline(object):

#    def __init__(self):
#       self.conn = pymongo.MongoClient(
#           'localhost',  # Enter the host
#           '27017'       # Enter the portnumber
#       )
#       db = self.conn['data']            # initialise the name of your database
#       self.collection = db['PG_1_tb']   # initialise the name of the table

#    def process_item(self, item, spider):
#        self.collection.insert(dict(item))
#        return item
# ----------------------------------------------------------------------------------------------------------------
