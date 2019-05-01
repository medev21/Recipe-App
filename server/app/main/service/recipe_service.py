import uuid
import datetime

from app.main import db
from app.main.model.recipe import Recipe

def save_new_recipe(data):
    #get recipe data
    new_recipe = Recipe(
        name = data['name'],
        description = data['description'],
        timestamp = datetime.datetime.utcnow()
    )

    #save recipe
    save_changes(new_recipe)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }

    return response_object, 201


def get_all_recipes():
    return Recipe.query.all()

def get_a_recipe(recipe_id):
    return Recipe.query.filter_by(recipe_id=recipe_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()