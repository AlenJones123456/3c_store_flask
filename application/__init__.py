from flask import Flask

from product import *
from sku import *
from transaction import *
from member import *

#建立Flask APP
def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    register_blueprints(app)
    register_extension(app)
    return app

#註冊API
def register_blueprints(app):
    app.register_blueprint(product_api, url_prefix="/3c_store/api/v1"+"/product")
    app.register_blueprint(sku_api, url_prefix="/3c_store/api/v1"+"/sku")
    app.register_blueprint(transaction_api, url_prefix="/3c_store/api/v1"+"/transaction")

#註冊擴充
def register_extension(app):
    db.init_app(app)