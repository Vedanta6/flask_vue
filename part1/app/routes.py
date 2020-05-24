from flask import jsonify
from app import app


@app.route('/')
@app.route('/index')
def index():
    shopping_list = [
        {
            'name': 'olive oil',
            'quantity': '1 bottle',
            'missing': True,
        },
        {
            'name': 'mozzarella cheese',
            'quantity': '250 g',
            'missing': True,
        },
        {
            'name': 'tomatoes',
            'quantity': '200 g',
            'missing': True,
        },
        {
            'name': 'basil',
            'quantity': '75 g',
            'missing': True,
        }
    ]
    return jsonify(
        {
            'status': 'success',
            'shopping_list': shopping_list
        }
    )
