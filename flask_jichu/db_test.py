#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

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

    #删
    article1 = Article.query.filter(Article.id == 1).first()
    db.session.delete(article1)
    db.session.commit()

    return 'hello'

if __name__ == '__main__':
    app.run()