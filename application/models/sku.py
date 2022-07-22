from db import db
from application.orm.sku import SkuORM
from sqlalchemy import select


class Sku(db.Model):
    
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