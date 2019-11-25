
# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_pymongo import PyMongo

# user session manager
from flask_login import LoginManager, login_manager

# Import debug toolbar
from flask_debugtoolbar import DebugToolbarExtension

# Define the WSGI application object
app = Flask(__name__,
            # instance_relative_config=True,
            # root_path='app',
            static_folder='_static',
            template_folder='_templates')

# Configurations
app.config.from_object('config.default')

# Define debug toolbar
TOOLBAR = DebugToolbarExtension(app)

# define login manager to the app
login_manager = LoginManager()
login_manager.init_app(app)


# define mongo connection manager to rhe app
mongo = PyMongo(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    """404 error handler
    """
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable
from app.blog.blogs import blog
from app.usuario.usuarios import usuario
from app.blog.posts import post
from app.sobre.sobre import sobre
# ...

# implementa array com as rotas e os blueprints, #lazyDev
ROUTES = [
    {'url_prefix': '/blogs',                 'blueprint': blog},
    {'url_prefix': '/blogs/<blog_id>/posts', 'blueprint': post},
    {'url_prefix': '/usuarios',              'blueprint': usuario},
    {'url_prefix': '/sobre',                 'blueprint': sobre},
]
# Register blueprint(s)
for route in ROUTES:
    # omitindo url_prefix
    # app.register_blueprint(route['blueprint'], url_prefix=route['url_prefx'])
    app.register_blueprint(route['blueprint'])
