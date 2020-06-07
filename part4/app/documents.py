from app import db


class ShoppingList(db.Document):
    name = db.StringField()
    quantity = db.FloatField()
    unit = db.StringField()
    missing = db.BooleanField()

    def __dict__(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'missing': self.missing
        }
