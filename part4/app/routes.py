from flask import jsonify, request
from app import app


SHOPPING_LIST = [
    {
        'name': 'olive oil',
        'quantity': 1,
        'unit': 'bottle(s)',
        'missing': True,
    },
    {
        'name': 'mozzarella cheese',
        'quantity': 250,
        'unit': 'g',
        'missing': True,
    },
    {
        'name': 'tomatoes',
        'quantity': 200,
        'unit': 'g',
        'missing': True,
    },
    {
        'name': 'basil',
        'quantity': 75,
        'unit': 'g',
        'missing': True,
    }
]


@app.route('/')
@app.route('/shoppinglist', methods=['GET', 'POST'])
def index():

    response_dict = {
        'status': 'success',
        'message': '',
        'shopping_list': SHOPPING_LIST
    }

    if request.method == 'POST':
        # update shopping list
        SHOPPING_LIST.clear()
        SHOPPING_LIST.extend(request.get_json())
        response_dict['message'] = 'List updated'
    else:
        # return default list
        response_dict['message'] = 'List acquired'

    return jsonify(response_dict)
