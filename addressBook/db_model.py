import sqlalchemy
print(sqlalchemy.__version__ )

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text


Base = declarative_base()
engine = create_engine('sqlite:///addressbook.db', echo=True)

class Contact(Base):
    __tablename__ = 'contacts'

    conid = Column(Integer, primary_key=True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    mobile_number = Column(String)
    address_text = Column(Text)

    def __init__(self, first_name, last_name, email, mobile_number, address_text):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_number = mobile_number
        self.address_text = address_text

    def __repr__(self):
       return "<User(first name='%s', last name='%s', email='%s', mobile number='%s', address=['%s'])>" % (
            self.first_name, self.last_name, self.email, self.mobile_number, self.address_text)

Base.metadata.create_all(engine)
    

