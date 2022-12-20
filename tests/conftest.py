import pytest
from recipebook_api.models import Recipe
from recipebook_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    recipe = Recipe('Test Recipe', 'Test Ingredients', 'Test Steps', 4, True)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()