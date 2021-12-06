# -*- coding: utf-8 -*-*
# @File : news.py
# @author : zjj
# @Time : 2021/12/06 18:26:03
#

from flask import Blueprint
new_list = Blueprint('news',__name__)


@new_list.route("/news")
def newlist():
    return "新闻模块"