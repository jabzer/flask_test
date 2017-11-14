#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app =  Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()