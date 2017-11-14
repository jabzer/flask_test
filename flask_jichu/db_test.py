#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)

#文章表
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref=db.backref('articles'))#引用和反向引用

db.create_all()

@app.route('/')
def index():
    # #增加：
    # article1 = Article(title='11月的第一天',content='天气晴朗')
    # db.session.add(article1)
    # #事务
    # db.session.commit()

    # #查
    # article1 = Article.query.filter(Article.title == '11月的第一天').first()
    # print(article1.title,article1.content)

    # #改
    # article1 = Article.query.filter(Article.title == '11月的第一天').first()
    # article1.content += '，没有下雨'
    # db.session.commit()

    # #删
    # article1 = Article.query.filter(Article.id == 1).first()
    # db.session.delete(article1)
    # db.session.commit()

    # #添加一个用户
    # user1 = User(username = 'admin')
    # db.session.add(user1)
    # db.session.commit()
    #
    # #添加一篇文章
    # article1 = Article(title='111',content='222',author_id='1')
    # db.session.add(article1)
    # db.session.commit()

    #通过文章找到作者
    article1 = Article.query.filter(Article.title == 'aaa').first()
    print(article1.author.username)
    #通过作者找到文章
    user = User.query.filter(User.username == 'admin').first()
    result = user.articles
    for article  in result:
        print(article.title,article.content)

    return 'hello'

if __name__ == '__main__':
    app.run()