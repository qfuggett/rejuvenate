"""CRUD operations."""

from model import db, User, Recipe, Ingredient, RecipeIngredient, Cleanse, UserCleanse, UserCleanseRecipe, CleanseLog, connect_to_db



def create_user(username, email, password):
    """Create and return a new user"""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()


def create_recipe(name, user):

    recipe = Recipe(name=name, user=user)

    db.session.add(recipe)
    db.session.commit()

    return recipe


def get_recipes():
    """Returns all recipes in database"""

    return Recipe.query.all()

def create_ingredient(name, calories):

    ingredient = Ingredient(name=name, calories=calories)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def get_ingredients():
    """Returns all ingredients in database"""

    return Ingredient.query.all()


def create_recipe_ingredient(recipe, ingredient):

    recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient)

    db.session.add(recipe_ingredient)
    db.session.commit()

    return recipe_ingredient


def get_recipe_ingredients():

    return RecipeIngredient.query.all()


def create_cleanse(start_date, end_date, public, description, user):

    cleanse = Cleanse(start_date=start_date, end_date=end_date, public=public, description=description, user=user)

    db.session.add(cleanse)
    db.session.commit()

    return cleanse


def get_cleanses():
    """Returns all cleanses in database"""

    return Cleanse.query.all()


def create_user_cleanse(active, completed, cleanse, user):

    user_cleanse = UserCleanse(active=active, completed=completed, cleanse=cleanse, user=user)

    db.session.add(user_cleanse)
    db.session.commit()

    return user_cleanse


def create_user_cleanse_recipe(timestamp, date, user_cleanse, recipe):

    user_cleanse_recipe = UserCleanseRecipe(timestamp=timestamp, date=date, user_cleanse=user_cleanse, recipe=recipe)

    db.session.add(user_cleanse_recipe)
    db.session.commit()

    return user_cleanse_recipe


def create_cleanse_log(timestamp, comment, private, user_cleanse):

    cleanse_log = CleanseLog(timestamp=timestamp, comment=comment, private=private, user_cleanse=user_cleanse)

    db.session.add(cleanse_log)
    db.session.commit()

    return cleanse_log






if __name__ == '__main__':
    from server import app
    connect_to_db(app)
