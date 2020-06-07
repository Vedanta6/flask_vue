from flask import jsonify, request, redirect, url_for
from app import app
from .documents import ShoppingList
from .manager import get_shopping_list, recreate_shopping_list, create_default_shopping_list


@app.route('/recreatedb', methods=['GET', 'POST'])
def recreatedb():
    if ShoppingList.objects.count() < 1:
        create_default_shopping_list()
    return redirect(url_for('shoppinglist'))


@app.route('/')
@app.route('/shoppinglist', methods=['GET', 'POST'])
def shoppinglist():

    response_dict = {
        'status': 'success',
        'message': '',
        'shopping_list': []
    }

    if request.method == 'POST':
        response_dict['shopping_list'] = recreate_shopping_list(request.get_json())
        response_dict['message'] = 'List updated'
    else:
        response_dict['shopping_list'] = get_shopping_list()
        response_dict['message'] = 'List acquired'

    return jsonify(response_dict)
