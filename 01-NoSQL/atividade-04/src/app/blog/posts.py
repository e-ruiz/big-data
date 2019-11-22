# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash
from pymongo import errors as mongo_errors
from bson.objectid import ObjectId
from flask_login import login_required
import datetime

from app import mongo


post = Blueprint('post', __name__)


@post.route('/novo', methods=['GET'])
@login_required
def get_novo(blog_id):
    data_hora = datetime.datetime.utcnow()
    return  render_template('blog/form-post.html', data_hora=data_hora, blog_id=blog_id)


@post.route('/novo', methods=['POST'])
@login_required
def post_novo(blog_id):
    novo_post = request.form
    data_hora = datetime.datetime.utcnow()

    try:
        post = mongo.db.blog.update_one({"_id": ObjectId(blog_id)}, 
        {"$set": {
            "titulo": request.form['titulo'],
            "data_hora": datetime.datetime.utcnow(),
            "secoes": [
                {
                    "titulo": "secao 1: %s" % request.form['titulo'],
                    "ordenacao": 1,
                    "conteudo": request.form['descricao'],
                    "subsecoes": [
                        {
                            "titulo": "",
                            "ordenacao": 1,
                            "conteudo": ""
                        }
                    ]
                }
            ]
        }})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    return 'ID: %s, post: %s, desc: %s, data: %s' % (blog_id, novo_post['titulo'], novo_post['descricao'], data_hora)


@post.route('', methods=['GET'])
def get_posts(blog_id):
    """Lista os posts
    """
    try:
        posts = mongo.db.blog.find_one({"_id": ObjectId(blog_id)}, {"posts": 1})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    return render_template('blog/post-detalhe.html', posts=posts[0], blog_id=blog_id)

