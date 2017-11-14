#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,url_for,redirect
import config

app =  Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return redirect(url_for('login'))
    return '首页'

@app.route('/login/')
def login():
    return '登录页面'

@app.route('/question/<is_login>')
def question(is_login):
    if is_login =='1':
        return '发布问答'
    else:
        return redirect(url_for('login'))


@app.route('/hello_world')
def hello_world():
    #url反转
    print(url_for('my_list'))
    print(url_for('article',id='addf'))
    return "hello world!"

#url传参数
@app.route('/article/<id>')
def article(id):
    return "你请求的参数是: %s"% id

#
@app.route('/list/')
def my_list():
    return 'list'



if __name__ == '__main__':
    app.run()