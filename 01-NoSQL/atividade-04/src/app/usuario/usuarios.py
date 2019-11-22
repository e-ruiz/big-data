# -*- coding: utf-8 -*-
"""
Flask Skeleton
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash
from pymongo import errors as mongo_errors
from bson.objectid import ObjectId
from flask_login import login_required, login_user, logout_user

from app import mongo, login_manager

from .model import Usuario


@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.get_by_id(usuario_id)


usuario = Blueprint('usuario', __name__)


@usuario.route('/', methods=['GET'])
def get_usuarios():
    """Lista os usuários cadastrados
    """
    usuarios = []
    try:
        usuarios = mongo.db.usuario.find()
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)
    
    return render_template('usuario/lista.html', usuarios=usuarios)


@usuario.route('/<usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    """Lista os usuários cadastrados
    """
    usuario = None
    try:
        # busca os dados do usuário, menos a SENHA!
        usuario = mongo.db.usuario.find_one({'_id': ObjectId(usuario_id)}, {'senha': 0})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)
    
    return render_template('usuario/detalhe.html', usuario=usuario)


@usuario.route('/novo', methods=['GET'])
def get_cadastro():
    """Form de cadastro do usuário/autor do blog
    """
    # flash('Hello!')
    # flash('outra mensagem')
    return render_template('usuario/form-cadastro.html', user={})


@usuario.route('/novo', methods=['POST'])
def post_cadastro():
    """Cadastro do usuário/autor
    """
    usuario = {
        "nome": request.form['nome'],
        "login": request.form['login'],
        "senha": request.form['senha']
    }

    try:
        user_id = mongo.db.usuario.insert(usuario)
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)
    
    flash('Cadastro criado com sucesso!')
    return redirect(url_for('usuario.get_cadastro_usuario', user_id=user_id))


@usuario.route('/<user_id>', methods=['GET'])
def get_cadastro_usuario(user_id):
    """Apresenta os dados de cadastro de um usuário específico
    """
    try:
        u = mongo.db.usuario.find_one_or_404({"_id": ObjectId(user_id)})
    except mongo_errors.OperationFailure as e:
        return render_template('db_error.html', error=e)

    usuario = {
        "nome": u['nome'],
        "login": u['login']
    }

    return render_template('usuario/perfil.html', perfil=usuario)

@usuario.route('/login', methods=['GET'])
def get_login():
    """Login do usuário
    """
    return render_template('usuario/login.html')


@usuario.route('/login', methods=['POST'])
def post_login():
    # try:
    #     login = mongo.db.usuario.find_one({
    #         "login": request.form['login'],
    #         "senha": request.form['senha'],
    #         })
    # except mongo_errors.OperationFailure as e:
    #     return render_template('db_error.html', error=e)
    
    usuario = Usuario(request.form['login'], request.form['senha'])

    if usuario.login():
        login_user(usuario)

        flash('Login efetuado com sucesso! Olá {}'.format(usuario.nome))
        return redirect(url_for('blog.get_blogs'))

    flash('Falha no login')
    return redirect(url_for('usuario.get_login'))


@usuario.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.get_blogs'))

# @usuario.route('/<user_id>', methods=['PUT'])
# def put_cadastro():
#     """PUT ou POST ?
#     """
#     return 'atualização de cadastro do autor/dono do blog'


# @usuario.route('/<user_id>', methods=['DELETE'])
# def delete_cadastro(user_id):
#     """Exclui um cadastro específico de usuário
#     (?) excluir todos os seus posts junto?
#     """
#     return 'exclusão do cadastro do autor/dono do blog'
