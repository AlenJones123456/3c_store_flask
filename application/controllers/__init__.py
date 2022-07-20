from flask import Blueprint
from flask_restful import Api

from .transaction import *
from .member import *
from .product import *

transaction_bp = Blueprint('transaction', __name__)
member_bp = Blueprint('member', __name__)
product_bp = Blueprint('product', __name__)
sku_bp = Blueprint('sku', __name__)

product_api = Api(product_bp)
transaction_api = Api(transaction_bp)
member_api = Api(member_bp)

transaction_api.add_resource(
    RestockController,
    RestockController.LIST_URL,
    RestockController.CREATE_URL
)
transaction_api.add_resource(
    RestockDataController,
    RestockDataController.LIST_URL,
    RestockDataController.CREATE_URL
)
transaction_api.add_resource(
    TransactionController,
    TransactionController.LIST_URL,
    TransactionController.CREATE_URL
)

transaction_api.add_resource(
    RestockDetailController,
    RestockDetailController.LIST_URL,
    RestockDetailController.CREATE_URL
)

member_api.add_resource(
    CustomerController,
    CustomerController.LIST_URL,
    CustomerController.CREATE_URL
)
member_api.add_resource(
    EmployeeController,
    EmployeeController.LIST_URL,
    EmployeeController.CREATE_URL
)

product_api.add_resource(
    ProductAPI,
    ProductAPI.LIST_URL
)

product_api.add_resource(
    AddProduct,
    AddProduct.LIST_URL
)

product_api.add_resource(
    ProductsList,
    ProductsList.LIST_URL
)

