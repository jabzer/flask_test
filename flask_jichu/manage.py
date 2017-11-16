# -*- coding: utf-8 -*-
from flask_script import Manager
from .db_test import app

manager = Manager(app=app)
@manager.command
def runserver():
    print()

if __name__=='__main__':
    manager.run()