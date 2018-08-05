from flask import current_app, flash
from flask_login import login_required, current_user

from . import web
from app.models.base import db
from app.models.gift import Gift


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('不要重复赠送书籍或添加愿望清单')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



