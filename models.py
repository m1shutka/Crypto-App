from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, BOOLEAN, LargeBinary
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase): pass
 
class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    item_price = Column(Integer)


class User(Base):
    __tablename__ = "users"
    record_id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    solt = Column(LargeBinary)
    isAdmin = Column(BOOLEAN)


class Keys(Base):
    __tablename__ = "keys"
    key_id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    isActivated = Column(BOOLEAN)


if __name__ == '__main__':
    Base.metadata.create_all(bind=create_engine("postgresql://postgres:postgres@localhost:5432/crypto"))
    pass
    #with Session(autoflush=False, bind=create_engine("postgresql://postgres:postgres@localhost:5432/crypto")) as db:

       #for i in range(3, 20):
            #db.add(Item(item_name=f'item{i}', item_price=i*100))     
       #db.commit() 

        #items = db.query(Params).all()
        #for i in items:
            #print(f"{i.rows} {i.levels} {i.cells}")



