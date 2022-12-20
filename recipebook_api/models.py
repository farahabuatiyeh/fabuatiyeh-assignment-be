from recipebook_api import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    steps = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    favourite = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.name

    def __init__(self, name, ingredients, steps, rating, favourite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        if rating >= 0 and rating <= 5:
            self.rating = rating
        else:
            self.rating = 0
        self.favourite = favourite