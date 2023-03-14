#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bakery, BakedGood

# db.init_app(app)

fake = Faker()

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    for i in range(20):
        b = Bakery(
            name=fake.company()
        )
        bakeries.append(b)
    
    db.session.add_all(bakeries)

    baked_goods = []
    names = []
    for i in range(200):

        name = fake.first_name()
        while name in names:
            name = fake.first_name()
        names.append(name)

        bg = BakedGood(
            name=name,
            price=randint(1,10),
            bakery=rc(bakeries)
        )

        baked_goods.append(bg)

    db.session.add_all(baked_goods)
    db.session.commit()
    
    most_expensive_baked_good = rc(baked_goods)
    most_expensive_baked_good.price = 100
    db.session.add(most_expensive_baked_good)
    db.session.commit()

#!/usr/bin/env python3

# from flask import Flask, make_response, jsonify
# from flask_migrate import Migrate

# from models import db, Bakery, BakedGood

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def index():
#     return '<h1>Bakery GET API</h1>'

# @app.route('/bakeries')
# def bakeries():
#     return ''

# @app.route('/bakeries/<int:id>')
# def bakery_by_id(id):
#     return ''

# @app.route('/baked_goods/by_price')
# def baked_goods_by_price():
#     return ''

# @app.route('/baked_goods/most_expensive')
# def most_expensive_baked_good():
#     return ''

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)