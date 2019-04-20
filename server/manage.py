# run.py

# local imports
import os
import unittest
from app.main import create_app, db

# library imports
from flask_script import Manager

config_name = os.getenv('RECIPE_ENV')
app = create_app(config_name or 'dev')

manager = Manager(app)

@manager.command
def run():
    app.run(port=5050)

@manager.command
def test():
    '''
    Run unit tests
    '''

    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    return 1

if __name__ == '__main__':
    manager.run()