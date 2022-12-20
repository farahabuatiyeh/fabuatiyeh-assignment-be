from recipebook_api import app
import pytest

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check if the response is valid
    """
    response = testing_client.get('/')
    assert response.status_code == 200

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check if the response is valid
    """   
    response = testing_client.post('/', json={'name': 'recipe1', 'ingredients': 'ingredient1', 'steps': 'step1', 'rating': 1, 'favourite': False})
    assert response.status_code == 200

def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/<id>' page is requested (GET)
    THEN check if the response is valid
    """
    response = testing_client.get('/1')
    assert response.status_code == 200

def test_edit_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/<id>' page is posted to (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/1', json={'name': 'recipe1', 'ingredients': 'ingredient1', 'steps': 'step1', 'rating': 1, 'favourite': False})
    assert response.status_code == 200

def test_delete_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<id>' page is posted to (DELETE)
    THEN check the response is valid
    """
    response = testing_client.delete('/1')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_dummy_wrong_method():
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.post('/')
        assert response.status_code == 400


