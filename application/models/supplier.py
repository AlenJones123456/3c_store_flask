# from db import db

# class Supplier(db.Model):
#     __tablename__ = 'supplier'
#     __table_args__ = {'mysql_charset': 'utf8mb4'}

#     supplier_id = db.Column(db.Integer, primary_key=True)
#     supplier_name = db.Column(db.String(40), nullable=False)
#     contact_num = db.Column(db.String(10), nullable=False)
#     create_time = db.Column(db.DateTime(), nullable=False)
#     last_instock_time = db.Column(db.DateTime(), nullable=False)

#     @classmethod 


#     def to_json(self):
#         json = {
#             'supplier_id': self.supplier_id,
#             'supplier_name': self.supplier_name,
#             'contact_num': self.contact_num,
#             'create_time': self.create_time.strftime("%m/%d/%Y, %H:%M:%S"),
#             'last_instock_time': self.last_instock_time.strftime("%m/%d/%Y, %H:%M:%S"),
#         }
#         return json
