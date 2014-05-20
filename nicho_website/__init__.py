from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from jinja2 import Environment, PackageLoader, TemplateNotFound

from utils import months

# @TODO implement cache
# from werkzeug.contrib.cache import SimpleCache


# create app
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='fake_secret',
    ))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# @TODO load cache
# cache = SimpleCache()

env = Environment(loader=PackageLoader('nicho_website', 'templates'))


# Handlers
@app.route('/')
def index():
    """
    Index page handler
    """
    return render_template('index.html')


@app.route('/blog/')
def blog():
    """
    The main blog handler
    """
    # @TODO make this a DB thing
    posts = [
        {'year': 2014, 'month': 5, 'slug': 'first-post',
            'title': 'First Post'}]
    return render_template('blog.html', posts=posts)


@app.route('/blog/<year>/<month>/<slug>')
def blog_article(year, month, slug):
    """
    Fetches a blog article
    """
    try:
        year = int(year)
        month = int(month)
    except Exception, e:
        return "Thats an error"

    try:
        template_path = "{year}/{month}/{slug}.html".format(
            year=year,
            month=month,
            slug=slug)

        time_of_writing = months[month] + " " + str(year)
        return render_template(template_path,
                               title="Test",
                               time_of_writing=time_of_writing)

    except TemplateNotFound, e:
        return error_404(e)


@app.route('/about')
def about():
    """
    The main about handler
    """
    return render_template('about.html')


@app.route('/projects')
def projects():
    """
    The main projects handler
    """
    return render_template('projects.html')


@app.errorhandler(404)
def error_404(e):
    return 'This was a 404: %s' % e
