from db import db
from application.orm.sku import SkuORM
from sqlalchemy import select


class Sku(db.Model):

    __tablename__ = 'sku'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    sku_id = db.Column(db.String(36), primary_key=True)
    product_id = db.Column(db.String(8), nullable=False)
    sku_code = db.Column(db.String(50), nullable=False)
    sell_price = db.Column(db.Integer, nullable=False)
    recom_price = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime(), nullable=False)
    update_time = db.Column(db.DateTime(), nullable=False)
    memo = db.Column(db.String(80), nullable=True)


    def __init__(self, sku_id, product_id, sku_code, sell_price, recom_price, cost, stock_quantity, create_time, update_time):
        self.sku_id=sku_id
        self.product_id=product_id
        self.sku_code=sku_code
        self.sell_price=sell_price
        self.recom_price=recom_price
        self.cost=cost
        self.stock_quantity=stock_quantity
        self.create_time=create_time
        self.update_time=update_time

    def to_sku_json(self):
        sku_json = {
            'sku_id': self.sku_id,
            'product_id': self.product_id,
            'sku_code': self.sku_code,
            'sell_price': self.sell_price,
            'recom_price': self.recom_price,
            'cost': self.cost,
            'stock_quantity': self.stock_quantity,
            'create_time': self.create_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'update_time': self.update_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'memo': self.memo
        }
        return sku_json

    def createSku_selectList():
         skurecord_list = db.session.query(Sku).all()

         SkuAdd_list_json = {
             'data': {
                'skurecord_list':{'sku_id':[record.sku_id for record in skurecord_list],
                                  'product_id':[record.product_id for record in skurecord_list],
                                  'sku_code':[record.sku_code for record in skurecord_list],
                                  'sell_price':[record.sell_price for record in skurecord_list],
                                  'recom_price':[record.recom_price for record in skurecord_list],
                                  'cost':[record.cost for record in skurecord_list],
                                  'stock_quantity':[record.stock_quantity for record in skurecord_list],}
                                 }, 
                                "title": "sku_create"
                      }
         
         return SkuAdd_list_json
    

    def skurecord_list(self):
        skurecord_list = db.session.query(select(self.product_id)).all()
        sku_json = {
            'skurecord_list': {
                'sku_id': [record.to_json() for record in skurecord_list],
                'product_id': [record.to_json() for record in skurecord_list],
                'sku_code': [record.to_json() for record in skurecord_list],
                'sell_price': [record.to_json() for record in skurecord_list],
                'recom_price': [record.to_json() for record in skurecord_list],
                'cost': [record.to_json() for record in skurecord_list],
                'stock_quantity': [record.to_json() for record in skurecord_list],
            }
            
        }  
        return sku_json