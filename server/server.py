from flask import Flask
from flask_restplus import Api,Resource
from flask_sqlalchemy import SQLAlchemy

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/recipedb'
db = SQLAlchemy(app=app)
api = Api(app=app)
ns = api.namespace('api', description='api operations')

@ns.route("/")
class RecipeList(Resource):
    
    def get(self):
        return {'hello': 'world'}



if __name__ == "__main__":
    app.run(port=5001)