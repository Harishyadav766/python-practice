from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation

Base = declarative_base()

class User(Base):
    __tablename__="person"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)
engine = create_engine('postgresql://postgres:Harish@123@localhost:5432/test')
#engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
'''
 __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     nickname = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
...                             self.name, self.fullname, self.nickname)

User.__table__ 
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('nickname', String(), table=<users>), schema=None)
'''
session = Session()
#user = User()
#user.id = 0
#user.username = "Alice"

#session.add(user)
#session.commit()

session.close()
