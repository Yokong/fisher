from flask import Flask


def create_app():
    """创建flask核心对象"""

    app = Flask(__name__)
    app.config.from_object('config')

    register_blueprints(app)
    return app


def register_blueprints(app):
    """注册蓝图"""

    from .web.book import web
    app.register_blueprint(web)
