# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, abort, flash, session
from pymongo import errors as mongo_errors
from bson.objectid import ObjectId
from bson.json_util import dumps as mongo_json_dumps
from flask_login import login_required, current_user
import datetime

from app import mongo, login_manager
from app.usuario.model import Usuario

@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.get_by_id(usuario_id)


secao = Blueprint('secao', __name__)


@secao.route('/secoes', methods=['GET'])
def get_secoes():
    return __name__


@secao.route('/blogs/<blog_id>/posts/<post_id>/secoes', methods=['GET'])
def get_secoes_novo(blog_id, post_id):
    """Detalha seções de um post específico
    """
    try:
        blog = mongo.db.blog.find_one(
            {
                '_id': ObjectId(blog_id), 
                'posts': {'$elemMatch': {'_id': ObjectId(post_id)}}
            },
            {'titulo': 1, 'posts.$': 1}
        )
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    data_cadastro = datetime.datetime.utcnow()
    return render_template(
        'secao/form-secao.html', 
        blog=blog, blog_id=blog_id, post_id=post_id, 
        data_cadastro=data_cadastro)



@secao.route('/blogs/<blog_id>/posts/<post_id>/secoes', methods=['POST'])
def post_secoes_novo(blog_id, post_id):
    return """
              Method: {}<br>
              Blog: {}<br>
              Post:{}<br>
              form: {}
              """.format(__name__, blog_id, post_id, request.form)
