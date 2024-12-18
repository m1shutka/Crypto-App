from ast import List
from models import Item, User, Keys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA256

class Manager():

    def __init__(self):
        self.__user_login = None
        self.__isAdmin = None


    def user_registration(self, user_login_reg: str, user_pass_reg: str, product_key: str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            exist_user = db.query(User).filter(User.login==user_login_reg).first()
            if exist_user == None:

                validate_key = db.query(Keys).filter(Keys.key==product_key).first()
                if validate_key != None and validate_key.isActivated != True:

                    validate_key.isActivated = True

                    cipher = Salsa20.new(key=b'\x9eKY\xaaT\xf10u7\xf8\xaf\x19\x8b7\x132E\x86\xb5V\xb3\xd1\x8b\nE\xac\x90\xa7/U\xa6\x81')
                    solt = cipher.nonce + cipher.encrypt(bytes(user_login_reg, 'utf-8'))
                    h = SHA256.new()
                    h.update(solt + bytes(user_pass_reg, 'utf-8'))

                    db.add(User(login=user_login_reg, solt=solt, password=h.hexdigest(), isAdmin=False))
                    db.commit()

                    return 'Зарегестрировано'

                else:
                    return 'Неверный ключ продукта!'
                    
            else:      
                return 'Пользователь с таким логином уже существует!'


    def user_autorization(self, user_login_auto: str, user_pass_auto:str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            user = db.query(User).filter(User.login==user_login_auto).first()
            if user != None:

                h = SHA256.new()
                h.update(user.solt + bytes(user_pass_auto, 'utf-8'))

                if user.password == h.hexdigest():
                    
                    self.__user_login = user.login

                    if user.isAdmin:
                        self.__isAdmin = True

                    else:
                        self.__isAdmin = False

                    return 'Вход успешен'
                else:
                    return 'Неверный логин или пароль!'
                    
            else:
                return 'Пользователя с таким логином не существует!'


    def get_items_list(self)->List:

        items_list = []

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            items = db.query(Item).filter(Item.item_name != None).all()
            for i in items:
                items_list.append(f'ID: {i.item_id}, название: {i.item_name}, цена: {i.item_price}')

        return items_list


    def isUserAdmin(self):
        return True if self.__isAdmin == True else False


    def userLogin(self):
        return self.__user_login


    def add_item(self, item_name_add:str, item_price_add:str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            item = db.query(Item).filter(Item.item_name==item_name_add).first()
            if item == None:
                item = db.query(Item).filter(Item.item_name==None).first()

                if item == None:
                    db.add(Item(item_name=item_name_add, item_price=int(item_price_add)))

                else:
                    item.item_name = item_name_add
                    item.item_price = int(item_price_add)
                db.commit()
                return 'Товар успешно добавлен!'

            else:
                return 'Товар с таким названием уже существует!'



    def delete_item(self, item_name_del: str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            item = db.query(Item).filter(Item.item_name==item_name_del).first()
            if item != None:
                db.delete(item)
                db.commit()
                return 'Товар успешно удален!'

            else:
                return 'Товара с таким названием не существует!'


    def quit(self):
        self.__user_login = None
        self.__isAdmin = None


    def sudo(self, user_login_sudo:str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            user = db.query(User).filter(User.login==user_login_sudo).first()
            if user != None:

                if not user.isAdmin:
                    user.isAdmin = True
                    db.commit()
                    return f'Поздравляем {user_login_sudo} с повышением!'

                else:
                    return 'Он уже админ... куда еще выше?'

            else:
                return 'Пользователя с таким логином не существует!'