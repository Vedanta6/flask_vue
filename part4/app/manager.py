from app import app
from .documents import ShoppingList


def into_float(item_dict, key):
    try:
        value = item_dict[key]
        return float(value)
    except (TypeError, KeyError):
        return -1


def into_bool(item_dict, key):
    try:
        value = item_dict[key]
        return value or str(value) in ['true', 'True']
    except (TypeError, KeyError):
        return True


def into_str(item_dict, key):
    try:
        value = item_dict[key]
        return value
    except KeyError:
        return ''


def create_shopping_list(shopping_list=None):
    if shopping_list is not None and isinstance(shopping_list, list):
        for item_dict in shopping_list:
            list_item = ShoppingList(
                name=into_str(item_dict, 'name'),
                quantity=into_float(item_dict, 'quantity'),
                unit=into_str(item_dict, 'unit'),
                missing=into_bool(item_dict, 'missing'),
            )
            list_item.save()


def create_default_shopping_list():
    default_list = [
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
    create_shopping_list(default_list)


def get_shopping_list():
    sl = ShoppingList.objects.all()
    return [si.__dict__() for si in sl]


def delete_shopping_list():
    [si.delete() for si in ShoppingList.objects.all()]


def recreate_shopping_list(shopping_list=None):
    if shopping_list is not None:
        delete_shopping_list()
        create_shopping_list(shopping_list)


@app.cli.command('delete-list')
def delete_list():
    delete_shopping_list()
    print(get_shopping_list())


@app.cli.command('create-default-list')
def create_default():
    create_default_shopping_list()
    print(get_shopping_list())


@app.cli.command('recreate-default-list')
def recreate_default():
    delete_shopping_list()
    create_default_shopping_list()
    print(get_shopping_list())


@app.cli.command('print-list')
def print_items():
    print(get_shopping_list())
