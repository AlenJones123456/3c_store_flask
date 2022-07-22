from db import db
from sqlalchemy import select

class ChkRecord(db.Model):
    __tablename__= 'chk_record'
    __table_args__={'mysql_charset': 'utf8mb4'}

    chkrec_id = db.Column(db.String(36), primary_key =True)
    sku_id = db.Column(db.String(36), nullable=False)
    chkstaff_id = db.Column(db.String(7), nullable=False)
    chk_date = db.Column(db.DateTime(), nullable=False)
    chk_amount = db.Column(db.Integer, nullable=False)


    @classmethod 
    def create(cls, chkrec_id, sku_id, chkstaff_id, chk_date, chk_amount):
        chk = ChkRecord()
        chk.chkrec_id = chkrec_id
        chk.sku_id = sku_id
        chk.chkstaff_id = chkstaff_id
        chk.chk_date = chk_date
        chk.chk_amount = chk_amount
        return chk

    def to_json(self):
        json = {
            'chkrec_id': self.chkrec_id,
            'sku_id': self.sku_id,
            'chkstaff_id': self.chkstaff_id,
            'chk_date': self.chk_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'chk_amount': self.chk_amount
        }
        return json

    def chkrecord_list(self):
        chkrecord_list = db.session.query(select(self.chkrec_id)).all()
        chk_json = {
            'chkrecord_list': {        
                'chkrec_id': [record.to_json() for record in chkrecord_list],
                'chkstaff_id': self.chkstaff_id,
            }
            
        }  
        return chk_json




