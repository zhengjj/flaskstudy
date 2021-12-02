# -*- coding: utf-8 -*-*
# @File : 2.py
# @author : zjj
# @Time : 2021/11/30 22:11:15
#

from flask import Flask,url_for,redirect

app = Flask(__name__)
@app.route('/')
def index():
    urltt = url_for('mylist')
    print(urltt)
    return redirect(urltt)
    

@app.route('/list/')
def mylist():
    return 'list'

if __name__ == '__main__':
    app.run()