"""Server for rejuvenate application"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from jinja2 import StrictUndefined
import crud


app = Flask(__name__)
app.secret_key = "sdDI2u*&"


@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/profile')
def user_profile():
    """User profile information"""

    return render_template('user_profile.html')


@app.route('/recipes')
def all_recipes():
    """Shows all cleanses, smoothies, and ingredients in database"""

    recipes = crud.get_recipes()
    ingredients = crud.get_ingredients()
    cleanses = crud.get_cleanses()
    recipe_ingredients = crud.get_recipe_ingredients()

    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, cleanses=cleanses, recipe_ingredients=recipe_ingredients)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)