from flask import Flask, request
from recipebook_api import db, app
from recipebook_api.models import Recipe


@app.route('/', methods=['POST'])
def create_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    rating = request.json['rating']
    favourite = request.json['favourite']
    recipe = Recipe(name, ingredients, steps, rating, favourite)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.route('/', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/<int:id>', methods=['PUT'])
def edit_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.steps = request.json['steps']
    recipe.rating = request.json['rating']
    recipe.favourite = request.json['favourite']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'rating': recipe.rating,
        'favourite': recipe.favourite
    }

