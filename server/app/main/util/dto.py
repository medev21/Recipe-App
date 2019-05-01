from flask_restplus import Namespace, fields

class RecipeDto:

    api = Namespace('recipe', description='recipe related operations')
    recipe = api.model('recipe', {
        'name': fields.String(required=True, description='recipe name'),
        'description': fields.String(required=True, description='recipe description')
    })