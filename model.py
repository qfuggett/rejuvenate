""" Models for application """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(15))
    location = db.Column(db.String(20))
    about = db.Column(db.Text)
    member_since = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} username={self.username}'


class Recipe(db.Model):
    """A recipe"""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(15), nullable=False)

    user = db.relationship('User', backref='recipes')

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} user_id={self.user_id} name={self.name}>'


class RecipeIngredient(db.Model):
    """Join table between recipes and ingredients"""

    __tablename__ = 'recipe_ingredients'

    recipe_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    recipe = db.relationship('Recipe', backref='recipe_ingredients')
    ingredient = db.relationship('Ingredient', backref='recipe_ingredients')

    def __repr__(self):
        return f'<RecipeIngredient recipe_ingredient_id={self.recipe_ingredient_id} recipe_id={self.recipe_id} ingredient_id={self.ingredient_id}>'


class Ingredient(db.Model):
    """An Ingredient"""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    food_data_id = db.Column(db.Integer)
    name = db.Column(db.String)
    calories = db.Column(db.Integer)

    def __repr__(self):
        return f'<Ingredient ingredient_id={self.ingredient_id} food_data_id={self.food_data_id} name={self.name} calories={self.calories}>'


class Cleanse(db.Model):
    """A Cleanse that tracks how long a user is consuming recipes/smoothies"""

    __tablename__ = 'cleanses'

    cleanse_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.Date)
    public = db.Column(db.Boolean)
    description = db.Column(db.Text)

    user = db.relationship('User', backref='cleanses')

    def __repr__(self):
        return f'<Cleanse cleanse_id={self.cleanse_id} user_id={self.user_id} start_date={self.start_date} end_date={self.end_date} public={self.public} description={self.description}>'


class UserCleanse(db.Model):
    """Associates a specific user with their cleanse"""

    __tablename__ = 'user_cleanses'

    user_cleanse_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cleanse_id = db.Column(db.Integer, db.ForeignKey('cleanses.cleanse_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    active = db.Column(db.Boolean)
    completed = db.Column(db.Boolean)

    cleanse = db.relationship('Cleanse', backref='user_cleanses')
    user = db.relationship('User', backref='user_cleanses')

    def __repr__(self):
        return f'<UserCleanse user_cleanse={self.user_cleanse_id} cleanse_id={self.cleanse_id} user_id={self.user_id} active={self.active} completed={self.completed}>'



class UserCleanseRecipe(db.Model):
    """Associates a recipe/smoothie with a cleanse"""

    __tablename__ = 'user_cleanse_recipes'

    user_cleanse_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_cleanse_id = db.Column(db.Integer, db.ForeignKey('user_cleanses.user_cleanse_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    timestamp = db.Column(db.Time)
    date = db.Column(db.DateTime)

    user_cleanse = db.relationship('UserCleanse', backref='user_cleanse_recipes')
    recipe = db.relationship('Recipe', backref='user_cleanse_recipes')

    def __repr__(self):
        return f'<UserCleanseRecipe user_cleanse_recipe_id={self.user_cleanse_recipe_id} user_cleanse_id={self.user_cleanse_id} recipe_id={self.recipe_id} timestamp={self.timestamp} date-{self.date}>'



class CleanseLog(db.Model):
    """Allows users to make comments about their cleanse throughout the day"""

    __tablename__ = 'cleanse_logs'

    cleanse_log_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_cleanse_id = db.Column(db.Integer, db.ForeignKey('user_cleanses.user_cleanse_id'))
    timestamp = db.Column(db.Time)
    comment = db.Column(db.Text, nullable=False)
    private = db.Column(db.Boolean)

    user_cleanse = db.relationship('UserCleanse', backref='cleanse_logs')

    def __repr__(self):
        return f'<CleanseLog cleanse_log_id={self.cleanse_log_id} user_cleanse_id={self.user_cleanse_id} timestamp={self.timestamp} comment={self.comment} private={self.private}>'



def connect_to_db(flask_app, db_uri='postgresql:///rejuvenate', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)