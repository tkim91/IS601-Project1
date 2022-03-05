from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

pages = Blueprint('pages', __name__,
                        template_folder='templates',static_folder='static')


@pages.route('/', defaults={'page': 'index'})
@pages.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
