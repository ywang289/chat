from flask import Flask, Response, request,flash, render_template, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from datetime import datetime
import math
import requests

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup


app=Flask(__name__)
CORS(app)

# app.config['SECRET_KEY']='zy112612' # 密码
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:zy112612@e6156-1.cudpmdtzmg9e.us-east-1.rds.amazonaws.com:3306/customer'
#     # 协议：mysql+pymysql
#     # 用户名：root
#     # 密码：2333
#     # IP地址：localhost
#     # 端口：3306
#     # 数据库名：runoob #这里的数据库需要提前建好
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# db=SQLAlchemy(app)


    
 
@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


 
@app.route('/add', methods=['GET','POST'])
def add_date():
    return render_template("new.html")
    

    

if __name__=='__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)