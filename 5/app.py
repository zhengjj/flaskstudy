# -*- coding: utf-8 -*-*
# @File : from.py
# @author : zjj
# @Time : 2021/12/08 18:08:20
#
from flask import Flask,url_for,render_template,flash
from flask import request
from flask_wtf import CSRFProtect
from forms import BaseLogin
import config

app = Flask(__name__)
app.config.from_object(config)
CSRFProtect(app)

print(app.config['SECRET_KEY'])

@app.route('/login',methods=('POST','GET'))
def baselogin():
    form=BaseLogin()
    print(request.method)
    if request.method =='POST':
        flash('||||||')
        print("ok")
        return '表格数据提交成功！'
    else:
        return render_template('from.html',form=form)

@app.route('/')
def index():
    return '首页'

if __name__ == '__main__':
    app.run(debug=True,port=8080)