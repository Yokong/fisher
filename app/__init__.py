from flask import Flask

from .models.book import db


def create_app():
    """创建flask核心对象"""

    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprints(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprints(app):
    """注册蓝图"""

    from .web.book import web
    app.register_blueprint(web)
