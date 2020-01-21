from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relation

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

def __ (self):
    return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

ed_user1 = User(id=1, name='harish', fullname='yadav', nickname='john')
ed_user2 = User(id=2, name='ram', fullname='kumar', nickname='kernal')
ed_user3 = User(id=3, name='hari', fullname='kkae', nickname='uscu')
ed_user4 = User(id=4, name='ish', fullname='qwfwef', nickname='owiueg')
ed_user5 = User(id=5, name='shrghhg', fullname='weffdvfh', nickname='kernal')
ed_user6 = User(id=6, name='kkka', fullname='jrefbdjcv', nickname='ldthr')
ed_user7 = User(id=7, name='jak', fullname='iwefuiwk', nickname='kayadev')
ed_user8 = User(id=8, name='har', fullname='mklkkoii', nickname='asfkjwbf')
'''
User.__table__ 
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('nickname', String(), table=<users>), schema=None)
'''
engine = create_engine('postgresql://postgres:Harish@123@localhost:5432/harish')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
#user = User()
#user.id = 0
#user.username = "Alice"

our_user6=session.query(User).filter_by(name='kkka').first()
our_user6

session.add(ed_user1)
session.add(ed_user2)
session.add(ed_user3)
session.add(ed_user4)
session.add(ed_user5)
session.add(ed_user6)
session.add(ed_user7)
session.add(ed_user8)

session.commit()
session.close()
