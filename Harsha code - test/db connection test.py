import sqlalchemy
import pymysql
import sqlalchemy as db
#get sqlalchemy and pymysql libraries
print("sqlalchemy : {}".format(sqlalchemy.__version__))
print("pymysql: {}".format(pymysql.__version__))
#get engine objects using mypysql
engine = db.create_engine("mysql+pymysql://root:Work@1234@localhost/harshadb")
#get connection object
connection = engine.connect()
#get meta data object
meta_data = db.MetaData()