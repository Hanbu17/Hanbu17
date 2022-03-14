import sqlalchemy
import pymysql
import sqlalchemy as db

def main():
    #get sqlalchemy and pymysql libraries
    print("sqlalchemy : {}".format(sqlalchemy.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    #get engine objects using mypysql
    engine = db.create_engine("mysql+pymysql://root:Qwerty1234@localhost/harshadb")
    #get connection object
    connection = engine.connect()
    #get meta data object
    meta_data = db.MetaData()
    # set train creation script table
    train = db.Table("train", meta_data,
    db.Column("x", db.Integer, primary_key=True, autoincrement=True,nullable=False),
    db.Column("y1(training func)", db.Float, nullable=False),
    db.Column("y2(training func)", db.Float, nullable=False),
    db.Column("y3(training func)", db.Float, nullable=False),
    db.Column("y4(training func)", db.Float, nullable=False)),
    #create train table and stores the information in metadata
    meta_data.create_all(engine)
if __name__ == '__main__':
    main()