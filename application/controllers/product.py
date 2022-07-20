# -*- coding: utf-8 -*-
from itertools import product
from urllib import response
from flask_restful import Resource, reqparse
from db_pyodbc import cnxn
from db import db
from ..models.product import Product
from ..models.brand import Brand
from ..models.category import Category
from ..models.member import Supplier

class ProductAPI(Resource):

    LIST_URL= '/product/<brand_id>'
    parser = reqparse.RequestParser()
    parser.add_argument('product_name', required=True, help='Product Name is required',location=['form'])
    parser.add_argument('product_model', required=True, help='Product Model is required',location=['form'])
    
    def get(self, brand_id):
        products = Product.query.filter_by(brand_id=brand_id).order_by(Product.product_id.desc()).all()
        json = {
            'Products': [record.to_json() for record in products]
        } 
        return json

    def post(self):
         # 新增資料
        try:
            arg =self.parser.parse_args()
            Product()
            product_add = Product('SP000011',f'{arg["product_name"]}',f'{arg["product_model"]}','B0002',1,4,'2022/01/01 20:37:21','蘋果14')
            db.session.add(product_add)
            db.session.commit()
            return {'message':f'insert {product_add}success'},200
        except Exception as e:
            print (e)
            return {"error message":f'{e}'}

    def put(self,date):
        # Update data
        product = Product.query.filter_by(product_name='iPhone 14').first()
        product.product_name = 'iPhone 14 Pro'
        db.session.commit()
        return 

    def delete(self,date):
        # 刪除資料
        query = Product.query.filter_by(product_name='iPhone 14').first()
        db.session.delete(query)
        db.session.commit()
        return 


class ProductsList(Resource):
    LIST_URL='/products/'
    parser = reqparse.RequestParser()
    parser.add_argument('product_name', required=True, help='Product Name is required',location=['form'])
    parser.add_argument('product_model', required=True, help='Product Model is required',location=['form'])
    
    def get(self):

        products = db.session.query(Product).all()
        json = {
            'Products': [record.to_json() for record in products]
        } 
        # query = Product.query.filter_by(brand_id='B0002').order_by(Product.product_id.desc()).all()
        # for record in query :
        #     print(record.product_id,record.product_name)
        return json

    def post(self):
         # 新增資料
        try:
            arg =self.parser.parse_args()
            product_add = Product('SP000011',f'{arg["product_name"]}',f'{arg["product_model"]}','B0002',1,4,'2022/01/01 20:37:21','蘋果14')
            db.session.add(product_add)
            db.session.commit()
            return {'message':f'insert {product_add}success'},200
        except Exception as e:
            print (e)
            return {"error message":f'{e}'}


class AddProduct(Resource):

    LIST_URL= '/addproduct/'
    parser = reqparse.RequestParser()
    parser.add_argument('product_name', required=True, help='Product Name is required',location=['form'])
    parser.add_argument('product_model', required=True, help='Product Model is required',location=['form'])
    
    def get(self):
        #多個物件
        brand_list = db.session.query(Brand).all()
        json = {
            'data': [record.to_json() for record in brand_list]
        } 
        return json

    def post(self):
         # 新增資料
        try:
            arg =self.parser.parse_args()
            Product()
            product_add = Product('SP000011',f'{arg["product_name"]}',f'{arg["product_model"]}','B0002',1,4,'2022/01/01 20:37:21','蘋果14')
            db.session.add(product_add)
            db.session.commit()
            return {'message':f'insert {product_add}success'},200
        except Exception as e:
            print (e)
            return {"error message":f'{e}'}

    def put(self,date):
        # Update data
        product = Product.query.filter_by(product_name='iPhone 14').first()
        product.product_name = 'iPhone 14 Pro'
        db.session.commit()
        return 

    def delete(self,date):
        # 刪除資料
        query = Product.query.filter_by(product_name='iPhone 14').first()
        db.session.delete(query)
        db.session.commit()
        return 
            