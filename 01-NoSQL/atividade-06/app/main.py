
# -*- coding: utf-8 -*-

from flask import Flask,render_template, request, abort
from flask_debugtoolbar import DebugToolbarExtension
from model  import Notas


app = Flask(__name__,
    # instance_relative_config=True,
    # root_path='app',
    static_folder='_static',
    template_folder='_templates')

app.config.from_object('config')

# Define debug toolbar
TOOLBAR = DebugToolbarExtension(app)


@app.route('/notas', methods=['POST'])
def post_notas():
    """Lista as notas
    """
    try:
       nota_id = int(request.form['nr_nota'])      
    except ValueError:
       return abort(400)
    else:        
        n = Notas()
        notas = n.get_itens_da_nota(nota_id)

        if not notas:
            return render_template('404.html')
        grid = {
            'id': 'grid-notas',
            'title': 'Notas',
            'class': 'grid  printable',
            'columns': {'nr': 'Número NF-e', 'cliente': 'Nome do Cliente'},
            'items': notas
        }

        return render_template('notas/lista.html', grid=grid)


@app.route('/notas', methods=['GET'])
def get_notas():
    return render_template('notas/form-consulta.html')


@app.route('/sobre', methods=['GET'])
def get_sobre():
    return render_template('notas/sobre.html')
