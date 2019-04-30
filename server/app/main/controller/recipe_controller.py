from flask import request
from flask_restplus import Resource

from ..util.dto import RecipeDto
from ..service.recipe_service import save_new_recipe, get_a_recipe, get_all_recipes

api = RecipeDto.api
_recipe = RecipeDto.recipe

@api.route('/')
class RecipeList(Resource):
    @api.doc('list_of_recipes')
    @api.marshal_list_with(_recipe, envelope='data')
    def get(self):
        '''
        List all recipes
        '''
        return get_all_recipes()

    @api.response(201, 'Recipe successfully created.')
    @api.doc('create a new recipe')
    @api.expect(_recipe, validate=True)
    def post(self):
        '''Creates a new recipe '''
        data = request.json
        return save_new_recipe(data=data)

@api.route('/<recipe_id>')
@api.param('recipe_id', 'The Recipe identifier')
@api.response(404, 'Recipe not found.')
class User(Resource):
    @api.doc('get a recipe')
    @api.marshal_with(_recipe)
    def get(self, recipe_id):
        """get a recipe given its identifier"""
        recipe = get_a_recipe(recipe_id)
        if not recipe:
            api.abort(404)
        else:
            return recipe