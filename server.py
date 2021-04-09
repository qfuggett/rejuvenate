"""Server for rejuvenate application"""

from flask import (Flask, render_template, request, flash, session, redirect, url_for)
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

    email = session['email']
    user = crud.get_user_by_email(email)
    

    return render_template('user_profile.html', user=user)


@app.route('/recipes')
def all_recipes():
    """Shows all cleanses, smoothies, and ingredients in database"""

    recipes = crud.get_recipes()
    ingredients = crud.get_ingredients()
    cleanses = crud.get_cleanses()
    recipe_ingredients = crud.get_recipe_ingredients()

    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, 
                            cleanses=cleanses, recipe_ingredients=recipe_ingredients)


@app.route('/recipe/<recipe_id>')
def recipe():
    """Shows specific recipe information"""


    return render_template('recipe_details.html')


@app.route('/user_recipes')
def user_recipes():
    """Shows cleanses, smoothies and recipes for the logged in user"""

    user_id = session['user_id']
    cleanses = crud.get_user_cleanses(user_id)


    return render_template('user_recipes.html', cleanses=cleanses)


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
        member_since = request.form.get('member_since')

        crud.create_user(username, email, password, name, location, about, member_since)
        flash('Account created! Please log in.')

        # flash('Cannot create an account with an existing email address. Try again')


        return redirect('/login')
    else:

        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User can login with existing account details"""

    if request.method == 'POST': #we want to retrieve data from the form and send it to the next
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = crud.get_user_by_email(email)
        session['username'] = username
        session['email'] = email
        session['user_id'] = user.user_id
        flash("Logged in as %s" % username)

        return render_template('user_profile.html', user=user)

    else: #just going to the /login page
        if 'user' in session:
            return redirect(url_for('user'))

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

    return redirect('/')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)