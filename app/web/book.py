from flask import jsonify, Blueprint, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key 
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

web = Blueprint('web', __name__)


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.packege_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.packege_collection(result, q)
        return jsonify(result)
    else:
        return jsonify({})
