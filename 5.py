# -*- coding: utf-8 -*-*
# @File : 5.py
# @author : zjj
# @Time : 2021/12/06 13:17:31
#

from flask import Flask,views,request
from flask.templating import render_template 
import time

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('5.1.html')

def runtime(func):
    def inner():
        stime=time.time()
        func()
        endtime=time.time()
        print("运行时间 %s"% endtime - stime )
    return inner

class loginView(views.MethodView):
    
    def get(self):
        print("get方法")
        time.sleep(2)
        return render_template('5.1.html')
    
    def post(self):
        username=request.form.get("username")
        password=request.form.get("password")
        print(username,password)
        if username == 'admin':
            return "欢迎管理员"
        else:
            return "错误！"

app.add_url_rule('/login',view_func=loginView.as_view('loginView'))


if __name__ == '__main__':
    app.run(debug=True)
    