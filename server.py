"""Server for rejuvenate application"""

from flask import (Flask, render_template, request, flash, session, redirect, url_for)
from model import connect_to_db
from jinja2 import StrictUndefined
from datetime import datetime
import crud
import requests 
import json
import os
import re



app = Flask(__name__)
app.secret_key = "sdDI2u*&"
app.jinja_env.add_extension('jinja2.ext.loopcontrols')



@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/profile')
def user_profile():
    """User profile information"""

    if 'user_id' not in session:
            return redirect('/login')

    email = session['email']
    user = crud.get_user_by_email(email)
    

    return render_template('user_profile.html', user=user)


@app.route('/recipes')
def all_recipes():
    """Shows all cleanses, smoothies, and ingredients in entire database"""

    recipes = crud.get_recipes()
    ingredients = crud.get_ingredients()
    cleanses = crud.get_cleanses()
    recipe_ingredients = crud.get_recipe_ingredients()

    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, 
                            cleanses=cleanses, recipe_ingredients=recipe_ingredients)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows ingredients of a specific recipe and allows user to start search to API to add an ingredient"""

    if 'user_id' not in session:
            return redirect('/login')

    recipe = crud.get_recipe_by_id(recipe_id)
    recipe_ingredients = crud.get_recipe_ingredients_by_id(recipe_id)

    
    return render_template('recipe_details.html', recipe=recipe, recipe_ingredients=recipe_ingredients)



@app.route('/recipe/<recipe_id>/add-ingredient', methods=['GET', 'POST'])
def add_ingredient_from_API(recipe_id):
    """Shows data from API and allows users to select their ingredients and post it to the database"""

    if request.method == 'POST':
        name_string = request.form.get('name')
        name = name_string.replace("/", "")
        calories_string = request.form.get('calories')
        calories = int(float(calories_string.replace("/", "")))
        recipe = crud.get_recipe_by_id(recipe_id)
        measurement = request.form.get('measurement')
        photo = request.form.get('photo')

        ingredient = crud.create_ingredient(name, calories, measurement, photo)
        crud.create_recipe_ingredient(recipe, ingredient)


        return redirect(f'/recipe/{recipe_id}')
    else:
        if 'user_id' not in session:
            return redirect('/login')

        search = request.args.get('name') #must use request.args.get for GET requests
        app_key = os.environ['app_key']
        app_id = os.environ['app_id']
        payload = {'ingr': search, 'app_id': app_id, 'app_key': app_key}
        url = 'https://api.edamam.com/api/food-database/v2/parser'
        res = requests.get(url, params=payload) #interacting directly with API
        data = res.json()
        ingredient = data['hints']

        return render_template('all_ingredients.html', ingredients=ingredient, recipe_id=recipe_id)


@app.route('/search')
def search():
    """Search API to simply show ingredients"""

    search = request.args.get('name') #must use request.args.get for GET requests
    app_key = os.environ['app_key']
    app_id = os.environ['app_id']
    payload = {'ingr': search, 'app_id': app_id, 'app_key': app_key}
    url = 'https://api.edamam.com/api/food-database/v2/parser'
    res = requests.get(url, params=payload) #interacting directly with API
    data = res.json()
    ingredient = data['hints']


    return render_template('all_ingredients.html', ingredients=ingredient, recipe_id=recipe_id)



@app.route('/add_recipe/<user_cleanse_id>', methods=['GET', 'POST'])
def add_recipe(user_cleanse_id):
    """Add a smoothie/recipe to a cleanse that already has recipes"""

    if request.method == 'POST':

        timestamp = datetime.now()
        date = datetime.now()
        user_cleanse = crud.get_user_cleanse(user_cleanse_id)

        recipe_name = request.form.get('recipe_name')
        ingredient_name = request.form.get('ingredient_name')
        calories = request.form.get('calories')
        measurement = request.form.get('measurement')
        user = crud.get_user_by_email(session['email'])
        photo = '/static/img/smoothie.jpg'

        recipe = crud.create_recipe(recipe_name, user)
        ingredient = crud.create_ingredient(ingredient_name, calories, measurement, photo)

        crud.create_recipe_ingredient(recipe, ingredient)
        crud.create_user_cleanse_recipe(timestamp, date, user_cleanse, recipe)

        return redirect('/user_cleanses') 
    else:
        if 'user_id' not in session:
            return redirect('/login')

        return render_template('add_recipe.html')


@app.route('/add_recipe_empty/<user_cleanse_id>', methods=['GET', 'POST'])
def add_recipe_empty(user_cleanse_id):
    """Add a smoothie/recipe to a cleanse that does not have any recipes"""

    if request.method == 'POST':

        timestamp = datetime.now()
        date = datetime.now()
        user_cleanse = crud.get_user_cleanse(user_cleanse_id)

        recipe_name = request.form.get('recipe_name')
        ingredient_name = request.form.get('ingredient_name')
        calories = request.form.get('calories')
        measurement = request.form.get('measurement')
        user = crud.get_user_by_email(session['email'])
        photo = "/static/img/smoothie.jpg"

        recipe = crud.create_recipe(recipe_name, user)
        ingredient = crud.create_ingredient(ingredient_name, calories, measurement, photo)

        crud.create_recipe_ingredient(recipe, ingredient)
        crud.create_user_cleanse_recipe(timestamp, date, user_cleanse, recipe)

        return redirect('/user_cleanses')
    else:
        if 'user_id' not in session:
            return redirect('/login')

        return render_template('add_recipe.html')



@app.route('/user_cleanses')
def user_cleanses():
    """Shows all cleanses for a specific user"""

    if 'user_id' not in session:
            return redirect('/login')

    user_id = session['user_id']
    user_cleanses = crud.get_user_cleanses(user_id)

    return render_template('user_cleanses.html', user_cleanses=user_cleanses)


@app.route('/cleanse/<user_cleanse_id>', methods=['GET', 'POST'])
def user_cleanse_recipes(user_cleanse_id):
    """Shows recipes/smoothies that belong to a specific cleanse and their ingredients
        Users can also submit an entry to their cleanse log for a specific cleanse"""

    if request.method == 'POST':

        timestamp = datetime.now()
        comment = request.form.get('comment')
        private = request.form.get('private')

        if private == 'on':
            private = False
        else:
            private = True

        user_cleanse = crud.get_user_cleanse(user_cleanse_id)
        crud.create_cleanse_log(timestamp, comment, private, user_cleanse)

        return redirect(f'/cleanse/{user_cleanse_id}')
    else:

        if 'user_id' not in session:
            return redirect('/login')

        user_cleanse = crud.get_user_cleanse(user_cleanse_id)
        user_cleanse_recipes = crud.get_user_cleanse_recipes(user_cleanse_id)
        session['user_cleanse_id'] = user_cleanse_id
        cleanse_logs = crud.get_cleanse_logs(user_cleanse_id)

        return render_template('cleanse_details.html', user_cleanse_recipes=user_cleanse_recipes, user_cleanse=user_cleanse, cleanse_logs=cleanse_logs)



@app.route('/start_cleanse', methods=['GET', 'POST'])
def start_cleanse():
    """Renders a form for a user to start a cleanse"""

    user = crud.get_user_by_email(session['email'])

    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        public = request.form.get('public')
        description = request.form.get('description')

        if public == 'on':
            public = True
        else:
            public = False

        cleanse = crud.create_cleanse(start_date, end_date, public, description, user)
        crud.create_user_cleanse(True, False, cleanse, user)


        return redirect('/user_cleanses')

    else:
        if 'user_id' not in session:
            return redirect('/login')

        return render_template('start_cleanse.html')




@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    """User can sign up for an account"""

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        location = request.form.get('location')
        about = request.form.get('about')
        member_since = datetime.now()

        if username or email or password == "":
            flash('Please complete all fields')

            return redirect('/signup')

        crud.create_user(username, email, password, name, location, about, member_since)
        flash('Account created! Please log in.')

        return redirect('/login')
    else:

        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User can login with existing account details"""

    if request.method == 'POST': 
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = crud.get_user_by_email(email)
        if user and password == user.password:
            session['username'] = username
            session['email'] = email
            session['user_id'] = user.user_id
            flash("Logged in as %s" % username)

            return render_template('user_profile.html', user=user)
        else:
            flash("Check your fields and try again.")
            return redirect('/login')

    else: 
        if 'user_id' in session:
            return redirect('/user')

        return render_template('login.html')


@app.route('/user')
def user():
    """Displays user profile page if logged in"""

    if 'user' in session:
        user = session['user']
        return render_template('user_profile.html')
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    """Logs the user out"""

    session.clear()
    # print(dir(session))
    flash('Successfully logged out')

    return redirect('/login')


@app.route('/community', methods=['GET', 'POST'])
def community():
    """Community Page that allows users to post a global comment or picture"""
    
    if request.method == 'POST':
        user = crud.get_user_by_id(session['user_id'])
        global_comment = request.form.get('comment')
        timestamp = datetime.now()
        comment = crud.create_global_comment(global_comment, timestamp, user)
        flash("Comment Posted!")

        return redirect('/community')
    else:
        if 'user_id' not in session:
            return redirect('/login')

        comments = crud.get_global_comments()

        return render_template('community.html', comments=comments)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)