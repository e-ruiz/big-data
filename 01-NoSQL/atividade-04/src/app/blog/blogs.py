# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from pymongo import errors as mongo_errors
from bson.objectid import ObjectId
from flask_login import login_required, current_user
import datetime

from app import mongo, login_manager
from app.usuario.model import Usuario


@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.get_by_id(usuario_id)


blog = Blueprint('blog', __name__)


@blog.route('/blogs', methods=['GET'])
def get_blogs():
    """Lista os blogs
    """
    try:
        # item 12
        blogs = mongo.db.blog.find().sort(
            [('posts.data_cadastro', -1
        )])

    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    return render_template('blog/lista.html', blogs=blogs)


@blog.route('/blogs/<blog_id>', methods=['GET'])
def get_blog(blog_id):
    """Lista um blog específico
    """
    try:
        b = mongo.db.blog.find_one_or_404({"_id": ObjectId(blog_id)})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    blog = {
        "titulo": b['titulo'],
        "descricao": b['descricao'],
        "data_cadastro": b['data_cadastro'],
        "posts": []
    }

    return render_template('blog/detalhe.html', blog=b)


@blog.route('/blogs/novo', methods=['GET'])
@login_required
def get_novo():
    """Apresenta o form de cadastro de blogs
    @todo: inserir o usuario/autor
    """
    return render_template('blog/form-blog.html')


@blog.route('/blogs/novo', methods=['POST'])
@login_required
def post_novo():
    """Registra um novo blog
    @todo: inserir o usuario/autor
    """
    blog = {
        "author_id": ObjectId(session['usr_id']),
        "titulo": request.form['titulo'],
        "descricao": request.form['descricao'],
        "data_cadastro": datetime.datetime.utcnow(),
        "posts": []
    }

    try:
        novo_blog = mongo.db.blog.insert_one(blog)
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    flash('Blog criado com sucesso!')
    return redirect(url_for('blog.get_blog', blog_id=novo_blog.inserted_id))



# @blog.route('/', methods=['GET'])
# def get_one_post(post_id)

# @blog.route('/post/novo', methods=['GET'])
# def get_form_post():
#     """form post/blog
#     """
#     return render_template('blog/form-blog.html')


# @blog.route('/post/novo', methods=['POST'])
# def post_form_post():
#     """Insere um novo post/blog
#     """
#     post = {
#         "titulo": request.form['titulo'],
#         "post": request.form['post']
#     }

#     try:
#         post_id = mongo.db.post.insert_one(post)
#     except mongo_errors.OperationFailure as e:
#         return render_template('db_error.html', error=e)
    
#     flash('Post criado com sucesso!')
#     return redirect(url_for('blog.get_post', post_id=post_id))

