from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# Converting a string to a url format, % -> %25
# from  urllib import parse
# print(parse.quote_plus("kx%jj5/g"))
engine = create_engine("sqlite:///:memory", echo=True)

# this create a class that inherit from sqlalchemy.orm.decl_api
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"
# represent this information for a specific table  using a "table object" 
print(repr(User.__table__))
Base.metadata.create_all(engine)
