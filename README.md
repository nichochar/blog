# Simple blog

Technologies used:
 * python (2 for now)
 * flask
 * sass for CSS
 * nginx


# Installation
You will not be able to use this as-is. For one thing you will need add a file in the root directory called
`blog/secret_utils.py` (it's .gitignore'd):
```
SECRET_KEY="keep this secret"
```

# Sass
Info [here](https://sass-lang.com/). You can install it pretty easily with npm and then write nicer CSS files
The basic compilation syntax is:
```
sass static/css/style.sass static/css/style.css
```
