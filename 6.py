from flask import Flask#导入Flask模块
import time
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
    return 'Hello World!'#返回值
def user_login(func):#定义视图函数
    def inner():#定义inner()函数
        starttime=time.time()
        func()#执行func函数
        time.sleep(2)
        endtime=time.time()
        print("%s函数运行时间为%s" % (func.__name__, endtime - starttime))
    return inner#返回inner函数
@user_login
@app.route('/news')
def news():#定义函数news
    print('这是新闻详情页!')#打印输出
    return "news"
# show_news=user_login(news)#news作为参数传递给user_login()函数
# show_news()#执行show_news()函数
user_login(news)
news()
if __name__ == '__main__':
    app.run()

