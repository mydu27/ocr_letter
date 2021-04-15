from __future__ import absolute_import
from flask import Flask
import config
from pymysql import install_as_MySQLdb
from app.plugins.private.orm import db


install_as_MySQLdb()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprint(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    db.init_app(app)
    print('xxxxxxxxxxx')
    with app.app_context():
        print('bbbbbbbbb')
        db.create_all(app=app)

    return app


def register_blueprint(app):
    """注册蓝图"""
    from app.api import __all__ as all_api
    for api in all_api:
        app.register_blueprint(api)
