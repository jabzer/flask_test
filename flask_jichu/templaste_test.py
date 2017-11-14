#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,url_for,redirect,render_template
import config

app =  Flask(__name__)
app.config.from_object(config)

@app.route('/6/')
def index_6():
    return render_template('6.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/5/')
def index_5():
    return render_template('5.html')

@app.route('/4/')
def index_4():
    comments = [
        {
            'user':'df','content':'哈哈'
        },
        {
            'user': 'df', 'content': '哈哈'
        },
        {
            'user': 'df', 'content': '哈哈'
        },
    ]
    av='http://www.quwj.com/wp-content/uploads/2017/09/maker.quwj_.banner.300.jpg'
    return render_template('4.html',av=av,comments=comments)

@app.route('/3/')
def index_3():
    user = {
        'username':'将该批',
        'age':189
    }
    websites = ['baidu.com','qq.com']
    books =[
        {
            'name':'西游记',
            'author':'吴承恩',
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
        },
        {
            'name': '三国演义',
            'author': '罗贯中',
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
        },
    ]
    return render_template('3.html',user=user,websites=websites,books=books)


@app.route('/2/<is_login>/')
def index_2(is_login):
    if is_login == '1':
        user = {
            'username' : '黄欧',
            'age': 89
        }
        return render_template('2.html',user = user)
    else:
        return render_template('2.html')

@app.route('/1/')
def index_1():
    class Person(object):
        name = '黄狗'
        age = 18
    p = Person()

    context = {
        'username':'李雷',
        'gender':'男',
        'age':'19',
        'person':p,
        'website':{
            'baidu':'www.baidu.com',
            'qq':'www.qq.com'
        }
    }
    return render_template('1.html',**context)

if __name__ == '__main__':
    app.run()