from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref = 'category', lazy = True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)



if __name__ == '__main__':
    from app import app
    with app.app_context():
        #c1 = Category(name='Mobile')
        #c2 = Category(name='Tablet')
        #db.session.add(c1)
        #db.session.add(c2)
        #db.session.commit()
        p1 = Product(name='Iphone 14', price=22000000,category_id=1, image='https://shopdunk.com/images/thumbs/0020316_iphone-15-pro-512gb.webp')
        p2 = Product(name='Ipad Pro 2022', price=24000000,category_id=2, image='https://shopdunk.com/images/thumbs/0020316_iphone-15-pro-512gb.webp')
        p3 = Product(name='Galaxy S3 Plus', price=27000000,category_id=1, image='https://shopdunk.com/images/thumbs/0020316_iphone-15-pro-512gb.webp')
        p4 = Product(name='Note 23+', price=21000000,category_id=1, image='https://shopdunk.com/images/thumbs/0020316_iphone-15-pro-512gb.webp')
        p5 = Product(name='Galaxy Tab S9', price=23000000,category_id=2, image='https://shopdunk.com/images/thumbs/0020316_iphone-15-pro-512gb.webp')
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()


        #db.create_all()