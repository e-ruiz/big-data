# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from pymongo import errors as mongo_errors
from bson.objectid import ObjectId
from flask_login import login_required
import datetime

from app import mongo, login_manager
from app.usuario.model import Usuario


@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.get_by_id(usuario_id)


post = Blueprint('post', __name__)


@post.route('/blogs/<blog_id>/posts/novo', methods=['GET'])
@login_required
def get_novo(blog_id):
    data_cadastro = datetime.datetime.utcnow()
    return  render_template('blog/form-post.html', data_cadastro=data_cadastro, blog_id=blog_id)


@post.route('/blogs/<blog_id>/posts/novo', methods=['POST'])
@login_required
def post_novo(blog_id):
    data_cadastro = datetime.datetime.utcnow()

    try:
        post = mongo.db.blog.update_one(
            {"_id": ObjectId(blog_id)}, 
            {"$push": {
                "posts": {
                    "_id": ObjectId(),
                    "titulo": request.form['titulo'],
                    "data_cadastro": data_cadastro,
                    "secoes": [{
                        "titulo": request.form['titulo'],
                        "data_cadastro": data_cadastro,
                        "conteudo": request.form['conteudo'],
                        "secoes": []
                    }]
                }
            }})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    return redirect(url_for('blog.get_blog', blog_id=blog_id))


 
# (?) @post.route('/posts/<post_id>', methods=['GET'])
@post.route('/blogs/<blog_id>/posts/<post_id>', methods=['GET'])
def get_post(blog_id, post_id):
    """Detalha um post específico
    """
    try:
        blog = mongo.db.blog.find_one(
            {
            "_id": ObjectId(blog_id), 
            'posts': {'$elemMatch': {'_id': ObjectId(post_id)}}
            }, 
            {"posts": 1}
        )
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    print(blog)
    return render_template('blog/post-detalhe.html', blog=blog, blog_id=blog_id)
