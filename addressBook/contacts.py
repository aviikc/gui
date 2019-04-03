from sqlalchemy import Column, Integer, String
from database import Base



class Contact(Base):
    __tablename__ = 'contacts'

    conid = Column(Integer, primary_key=True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    mobile_number = Column(String(10))
    address_text = Column(String(255))

    def __init__(self, first_name=None, last_name=None, email=None, mobile_number=None, address_text=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_number = mobile_number
        self.address_text = address_text    

    def __repr__(self):
       return "<User(first name='%s', last name='%s', email='%s', mobile number='%s', address=['%s'])>" % (
            self.first_name, self.last_name, self.email, self.mobile_number, self.address_text)