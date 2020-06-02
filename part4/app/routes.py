from flask import jsonify, request
from app import app
from .manager import get_shopping_list, recreate_shopping_list


@app.route('/')
@app.route('/shoppinglist', methods=['GET', 'POST'])
def index():

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
