# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, render_template
from flask_login import login_required


sobre = Blueprint('sobre', __name__)


@sobre.route('', methods=['GET'])
def get_sobre():
    """Descrição do trabalho
    """
    return render_template('sobre/sobre.html')

