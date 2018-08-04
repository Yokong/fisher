from flask import Flask
from flask_login import LoginManager

from .models.base import db

login_manager = LoginManager()


def create_app():
    """创建flask核心对象"""

    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprints(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录/注册'
    with app.app_context():
        db.create_all()
    return app


def register_blueprints(app):
    """注册蓝图"""

    from .web.book import web
    app.register_blueprint(web)
