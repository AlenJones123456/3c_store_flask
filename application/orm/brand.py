from db import db
from sqlalchemy import select

class Brand(db.Model):
    __tablename__ = 'brand'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    brand_id = db.Column(db.String(5),primary_key=True)
    brand_code = db.Column(db.String(2), nullable=True)
    brand_name = db.Column(db.String(64), nullable=True)

    db_brand_product = db.relationship("Product", backref="brand")

    def to_json(self):
        json = {
            'brand_id': self.brand_id,
            'brand_code': self.brand_code,
            'brand_name': self.brand_name,
        }
        return json
