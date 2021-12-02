# -*- coding: utf-8 -*-*
# @File : 1.py
# @author : zjj
# @Time : 2021/11/30 17:00:59
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD!'
@app.route('/name/<name>')
def list_name(name):
    a="super" + name
    return 'name :%s' % a


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)