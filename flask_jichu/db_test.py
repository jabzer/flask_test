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
    return 'hello'

if __name__ == '__main__':
    app.run()