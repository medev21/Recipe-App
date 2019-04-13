from flask import Flask
from flask_restplus import Api,Resource

app = Flask(__name__)
api = Api(app=app)
ns = api.namespace('api', description='api operations')

@ns.route("/")
class RecipeList(Resource):
    
    def get(self):
        return {'hello': 'world'}



if __name__ == "__main__":
    app.run(debug=True)