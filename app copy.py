# API é um lugar para disponibilizar recursos e/ou funcionalidades no Backend.
# 1 - Objetivo => Consulta, Criação, Edição e Exclusão de itens de um data_json.
# 2 - URL base => Será hospedado no Local Host.
# 3 - Endpoints =>
        # - localhost/data_json (GET - Vai disponibilizar todos os itens)
        # - localhost/data_json (POST - Para criar novo item no data_json)
        # - localhost/data_json/id (GET por ID - Vai consultar o data_jsons especificamente por ID)
        # - localhost/data_json/id (PUT para MODIFICAR um item do data_json - para editar um item)
        # - localhost/data_json/id (DELETE - para exclusão de itens do data_json)

# 4 - Quais recursos iremos utilizar/disponibilizar => data_json contendo dados de clientes.

import json
from flask import Flask, jsonify, request

app = Flask(__name__)

data_json = []

# Obtendo os dados de um JSON externo
@app.route('/')
def get_data_json():
    global data_json
    with open('clients.json') as file:
        data_json = json.load(file)
    return jsonify(data_json)

# Consultar (Todos itens):
@app.route('/data_json', methods=['GET'])
def get_items():
    return jsonify(data_json) 

# Criar (Novo item)
@app.route('/data_json', methods=['POST'])
def create_item():
    new_item = request.get_json()
    data_json.append(new_item)
    return jsonify(data_json) 

# Consultar (por id do item)
@app.route('/data_json/<int:id>', methods=['GET'])
def get_item_by_id(id):
    for item in data_json:
        if item.get('id') == id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'})

# Editar (item)
@app.route('/data_json/<int:id>', methods=['PUT'])
def edit_item_by_id(id):
    edited_item = request.get_json()
    for index, item in enumerate(data_json):
        if item.get('id') == id:
            data_json[index].update(edited_item)
            return jsonify(data_json[index])
    return jsonify({'error': 'Item not found'})

# Excluir (item)
@app.route('/data_json/<int:id>', methods=['DELETE'])
def delete_item(id):
    for index, item in enumerate(data_json):
        if item.get('id') == id:
            del data_json[index]
            return jsonify(data_json)
    return jsonify({'error': 'Item not found'})

# Rodar a aplicação
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)


