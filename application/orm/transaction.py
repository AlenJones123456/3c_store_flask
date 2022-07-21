from db import db


class Transaction(db.Model):
    __tablename__ = 'trans_record'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    trans_id = db.Column(db.String(36), primary_key=True)
    employee_id = db.Column(db.String(7), nullable=False)
    customer_id = db.Column(db.String(7), nullable=False)
    trans_date = db.Column(db.DateTime(), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    @classmethod 
    def create(cls, trans_id, employee_id, customer_id, trans_date, total_price):
        transaction = Transaction()
        transaction.trans_id = trans_id
        transaction.employee_id = employee_id
        transaction.customer_id = customer_id
        transaction.trans_date = trans_date
        transaction.total_price = total_price
        return transaction

    def to_json(self):
        json = {
            'trans_id': self.trans_id,
            'employee_id': self.employee_id,
            'customer_id': self.customer_id,
            'trans_date': self.trans_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'total_price': self.total_price
        }
        return json



class ReStock(db.Model):
    __tablename__ = 'restock_record'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    restock_id = db.Column(db.String(36), primary_key=True)
    employee_id = db.Column(db.String(7), nullable=False)
    supplier_id = db.Column(db.String(7), nullable=False)
    restock_date = db.Column(db.DateTime(), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    @classmethod 
    def create(cls, restock_id, employee_id, supplier_id, restock_date, total_price):
        restock = ReStock()
        restock.restock_id = restock_id
        restock.employee_id = employee_id
        restock.supplier_id = supplier_id
        restock.restock_date = restock_date
        restock.total_price = total_price
        return restock

    def to_json(self):
        json = {
            'restock_id': self.restock_id,
            'employee_id': self.employee_id,
            'supplier_id': self.supplier_id,
            'restock_date': self.restock_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'total_price': self.total_price
        }
        return json

class ReStockDetail(db.Model):
    __tablename__ = 'restock_detail'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    restock_id = db.Column(db.String(36), primary_key=True)
    sku_id = db.Column(db.String(11), primary_key=True, nullable=False)
    serial_id = db.Column(db.String(128), nullable=True)
    sale_price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    memo = db.Column(db.String(300), nullable=True)

    @classmethod 
    def create(cls, restock_id, sku_id, serial_id, sale_price, quantity, memo):
        restock_detail = ReStockDetail()
        restock_detail.restock_id = restock_id
        restock_detail.sku_id = sku_id
        restock_detail.serial_id = serial_id
        restock_detail.sale_price = sale_price
        restock_detail.quantity = quantity
        restock_detail.memo = memo
        return restock_detail

    def to_json(self):
        json = {
            'restock_id': self.restock_id,
            'sku_id': self.sku_id,
            'serial_id': self.serial_id,
            'sale_price': self.sale_price,
            'quantity': self.sale_quantity,
            'memo': self.memo
        }
        return json