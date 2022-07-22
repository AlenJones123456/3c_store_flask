from db import db
from application.models.chkrecord import ChkRecord
from application.orm.sku import SkuORM


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
        chkrecord_list = db.session.query(ChkRecord).all()

        SkuAdd_list_json = {
            'data': {
                'chkrecord_list':{'chkrec_id':[record.chkrec_id for record in chkrecord_list],
                            'chk_staff':[record.chkstaff_id for record in chkrecord_list]
                }, 
                "title": "sku_create"
            }
        }
        return SkuAdd_list_json