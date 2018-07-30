import json

from flask import jsonify, Blueprint, request, render_template, flash

from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key 
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
    else:
        flash('无效的关键词')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass
