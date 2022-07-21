from db import db

class ChkRecord(db.Model):
    __tablename__= 'chkrecord'
    __table_args__={'mysql_charset': 'utf8mb4'}

    chkrec_id = db.Column(db.string(36), primary_key =True)
    sku_id = db.Column(db.string(36), nullable=False)
    chkstaff_id = db.Column(db.string(7), nullable=False)
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



