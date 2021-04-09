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

    return render_template('user_profile.html')


@app.route('/recipes')
def all_recipes():
    """Shows all cleanses, smoothies, and ingredients in database"""

    recipes = crud.get_recipes()
    ingredients = crud.get_ingredients()
    cleanses = crud.get_cleanses()
    recipe_ingredients = crud.get_recipe_ingredients()

    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, 
                            cleanses=cleanses, recipe_ingredients=recipe_ingredients)


@app.route('/signup', methods=['GET'])
def sign_up():
    """User can sign up for an account"""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    # if user:
    #     flash('Cannot create an account with an existing email address. Try again')
    # else:
    #     crud.create_user(username, email, password)
    #     flash('Account created! Please log in.')

    return render_template('signup.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User can login with existing account details"""

    if request.method == 'POST': #we want to retrieve data from the form and send it to the next
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        session['user'] = username
        flash("Logged in as %s" % username)

        return redirect(url_for('user', user=username))

    else: #just going to the /login page
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

    session.pop('user', None)

    return redirect('/login')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)