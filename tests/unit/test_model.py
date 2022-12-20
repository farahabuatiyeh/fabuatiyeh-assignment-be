from recipebook_api.models import Recipe
import pytest

def test_create_recipe():

    recipe = Recipe('Pesto Pasta', 'Water, Olive Oil, Garlic, Pesto Sauce, Creme, Penne, Parmesan, Salt, Pepper, Italian Spices', 'Boil water, put the pasta till it is cooked. On the side, put a pan with olive oil, garlic. Add your pesto sauce, then some cream, add the spices, then add the pasta and serve!', 4, True)
    assert recipe.name == 'Pesto Pasta'
    assert recipe.ingredients == 'Water, Olive Oil, Garlic, Pesto Sauce, Creme, Penne, Parmesan, Salt, Pepper, Italian Spices'
    assert recipe.steps == 'Boil water, put the pasta till it is cooked. On the side, put a pan with olive oil, garlic. Add your pesto sauce, then some cream, add the spices, then add the pasta and serve!'
    assert recipe.rating == 4
    assert recipe.favourite == True