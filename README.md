# Nicholas' blog

This is the source code for my blog, that I host on a [digital ocean box](https://m.do.co/c/e1c4aa70f263), which is a service that I highly recommend.

Technology stack:
 * python (2 for now)
 * [flask & jinja2](https://flask.palletsprojects.com/en/1.1.x/)
 * [sass](https://sass-lang.com/) for CSS
 * [nginx](https://docs.nginx.com/nginx/)


# Installation
You will need to add `SECRET_KEY` to `blog/secret_utils.py` (.gitignore'd):
```
SECRET_KEY="keep this secret"
```

# Development
You can run the development server with
```
python run.py
```

# Watching CSS files with sass
Info [here](https://sass-lang.com/). You can install it pretty easily with npm and then write nicer CSS files
The basic compilation syntax is:
```
sass static/css/style.sass static/css/style.css
```
