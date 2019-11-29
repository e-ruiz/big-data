# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, abort, flash, session
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
        blog = mongo.db.blog.find({
                '_id': ObjectId(blog_id)
            }).sort([('posts.data_cadastro', -1)])
        if blog.count() <= 0:
            return abort(404)
        blog = blog[0]
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    # blog = {
    #     'titulo': b[0]['titulo'],
    #     'descricao': b[0]['descricao'],
    #     'data_cadastro': b[0]['data_cadastro'],
    #     'posts': []
    # }

    return render_template('blog/detalhe.html', blog=blog)


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


