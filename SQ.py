from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('postgresql:///test.db', echo=True)
Base = declarative_base(engine)

meta=MetaData()
conn = engine.connect()
students = Table('students', meta, Column('id', Integer, primary_key=True),
Column('name', String), Column('lastname', String),)
addresses=Table('addresses', meta, Column('id', Integer, primary_key=True),
Column('st_id', Integer,ForeignKey('students.id')), Column('postal_add',
String), Column('email_add', String))
from sqlalchemy import join
from sqlalchemy.sql import select
j = students.join(addresses, students.c.id == addresses.c.st_id)
stmt = select([students]).select_from(j)
result=conn.execute(stmt)
result.fetchall()

