import socket
from flask import Flask
from flask import render_template
from jinja2 import Environment, PackageLoader, TemplateNotFound

from utils import months, get_title_from_slug
from articles import articles_data
from secret_utils import SECRET_KEY

# @TODO implement cache
# from werkzeug.contrib.cache import SimpleCache
IS_PRODUCTION = socket.gethostname() == 'nicholascharriere'


# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config
app.config.update(dict(
    DEBUG=not IS_PRODUCTION,
    SECRET_KEY=SECRET_KEY,
    ))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# @TODO load cache
# cache = SimpleCache()

env = Environment(loader=PackageLoader('blog', 'templates'))


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
    return render_template('blog.html', articles_data=articles_data)


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
        title = get_title_from_slug(slug)

        if not title:
            title = "No title"

        return render_template(template_path,
                               title=title,
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
