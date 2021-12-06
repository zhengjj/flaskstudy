# -*- coding: utf-8 -*-*
# @File : 6.py
# @author : zjj
# @Time : 2021/12/06 18:25:22
# 蓝图

from flask import Flask
import news


app = Flask(__name__)
@app.route('/')
def hello():
    return "首页"

app.register_blueprint(news.new_list)

if __name__ == '__main__':
    app.run(debug=True)