import socket
import os
import random
import json

from flask import Flask
from flask import render_template
from jinja2 import Environment, PackageLoader, TemplateNotFound

from blog.utils import MONTHS, get_title_from_slug
from blog.secret_utils import SECRET_KEY

IS_PRODUCTION = socket.gethostname() == 'nicholascharriere'


# Initialize app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# Load default config
app.config.update(dict(DEBUG=not IS_PRODUCTION, SECRET_KEY=SECRET_KEY))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
env = Environment(loader=PackageLoader('blog', 'templates'))

ARTICLES_PATH = os.path.join(app.root_path, 'articles.json')
with open(ARTICLES_PATH, 'r') as f:
    articles_data = json.load(f)
app.config.update(articles=articles_data)


# Handlers
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog/')
def blog():
    return render_template('blog.html', articles_data=reversed(app.config["articles"]))


@app.route('/blog/<year>/<month>/<slug>')
def blog_article(year, month, slug):
    try:
        year = int(year)
        month = int(month)
    except Exception as e:
        return error_404(e)

    try:
        template_path = f"articles/{slug}.html"
        time_of_writing = MONTHS[month] + " " + str(year)
        title = get_title_from_slug(slug, app.config["articles"]) or 'No title'

        return render_template(template_path, title=title, time_of_writing=time_of_writing)

    except TemplateNotFound as e:
        return error_404(e)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/python')
def python():
    import sys
    return str(sys.version_info)


@app.route('/resume')
def resume():
    return app.send_static_file('pdf/CV.pdf')


@app.route('/cv')
def cv():
    return app.send_static_file('pdf/CV.pdf')


@app.route('/treestumps')
def treestumps():
    directory = 'blog/static/treestumps'
    files = os.listdir(directory)
    files = [f for f in files if 'jpg' in f]
    random.shuffle(files)
    files_and_sizes = []
    for elt in files:
        files_and_sizes.append({
            'name': os.path.join('treestumps', elt),
            'size': random.randint(1, 3),
        })
    return render_template('treestumps.html', files=files_and_sizes)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    r.headers["X-Served-By-Flask"] = "true"
    return r


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html')
