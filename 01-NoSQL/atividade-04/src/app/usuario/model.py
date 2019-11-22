# -*- coding: utf-8 -*-
"""
@see https://flask-login.readthedocs.io/en/latest/#configuring-your-application
"""

from app import mongo
from pymongo import errors as mongo_errors
from bson import ObjectId


class Usuario():
    def __init__(self, login, senha=None, nome=''):
        self.nome = nome
        self.nome_de_usuario = login
        self.senha = senha

        self.id = None
        self._is_autenticated = False


    def get_by_id(usuario_id):
        usr = mongo.db.usuario.find_one({'_id': ObjectId(usuario_id.decode())}, {'senha': False})
        
        if usr:
            u = Usuario(usr['login'])
            u.nome = usr['nome']
            u.nome_de_usuario = usr['login']
            return u
        return None


    def login(self):
        """Tenta validar login e senha no MongoDB.
        Retorna True se validar, se não, retorna False.
        Caso ocorra, retorna a exceção do banco.
        """
        try:
            usuario = mongo.db.usuario.find_one({'login': str(self.nome_de_usuario), 'senha': str(self.senha)})
            if usuario:
                self.id = str(usuario['_id'])
                self.nome = usuario['nome']
                self.is_anonymous = False
                self._is_autenticated = True and self.is_active()
                return True

        except mongo_errors.OperationFailure as e:
            raise e

        return False


    def is_authenticated(self):
        """This property should return True if the user is authenticated, 
        i.e. they have provided valid credentials. 
        (Only authenticated users will fulfill the criteria 
        of login_required.)
        """
        return self._is_autenticated


    def is_active(self):
        """This property should return True if this is an active user 
        - in addition to being authenticated, they also have activated 
        their account, not been suspended, or any condition your 
        application has for rejecting an account. 
        Inactive accounts may not log in (without being forced of course).
        """
        # @todo: implementar controle avançado de usuário
        return True


    def is_anonymous(self):
        """This property should return True if this is an anonymous user. 
        (Actual users should return False instead.)
        """
        return True if self.id else False


    def get_id(self):
        """This method must return a unicode that uniquely 
        identifies this user, and can be used to load the user from the 
        user_loader callback. Note that this must be a unicode - 
        if the ID is natively an int or some other type, 
        you will need to convert it to unicode. 
        """
        return self.id.encode()

