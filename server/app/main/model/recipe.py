from .. import db, flask_bcrypt

class Recipe(db.Model):
    '''
    Recipe Model for storing recipe details
    '''

    __tablename__ = "recipe"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # print out recipe class
    def __repr__(self):
        return "<recipe name '{}".format(self.name)

    # #constructor
    # def __init__(self, name, description):
    #     self.name =  name
    #     self.description = description