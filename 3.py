# -*- coding: utf-8 -*-*
# @File : 3.py
# @author : zjj
# @Time : 2021/12/01 10:36:54
#

from flask import Flask,render_template
from flask.sessions import NullSession


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/",strict_slashes=False)
@app.route("/user/<username>")
def user(username=''):
    if username!='':
        username=username
    else:
        username=''
    usertile='VIP'
    return render_template("user.html",**locals())

if __name__ == "__main__":
    app.run(debug=True,port=8080)