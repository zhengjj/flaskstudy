# -*- coding: utf-8 -*-*
# @File : 4.py
# @author : zjj
# @Time : 2021/12/02 16:56:04
#

from os import name
from flask import Flask,render_template_string
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    books={'bookname':'test01','bookauthor':'my','pages':99}
    return render_template('4.html',**locals())

@app.route('/99/')
def cf99():
    num = range(1,10)
    return render_template('5.html',**locals())

if __name__=='__main__':
    app.run(port=8080)