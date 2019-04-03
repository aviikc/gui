from sqlalchemy import Column, Integer, String
from database import Base



class Commerce(Base):
    __tablename__ = 'commerce'

    comid = Column(Integer, primary_key=True)
    shopname = Column(String, nullable = False)
    email = Column(String, nullable = False, unique=True)
    mobile_number = Column(String(10))
    shop_type = Column(String(50))

    def __init__(self, shopname = None, email = None, mobile_number = None, shop_type = None):
        self.shopname = shopname
        self.email = email
        self.mobile_number = mobile_number
        self.shop_type = shop_type    

    def __repr__(self):
       return "<User(shopname ='%s', email='%s', mobile number='%s', Shop Type='%s')>" % (
            self.shopname, self.email, self.mobile_number, self.shop_type)