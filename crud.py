"""CRUD operations."""

from model import db, User, Recipe, Ingredient, RecipeIngredient, Cleanse, UserCleanse, UserCleanseRecipe, CleanseLog, connect_to_db



def create_user(username, email, password, name, location, about, member_since):
    """Create and return a new user"""

    """IN USE"""

    user = User(username=username, email=email, password=password, name=name, location=location, about=about, member_since=member_since)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by email"""

    """IN USE"""

    return User.query.filter(User.email == email).first()


def create_recipe(name, user):
    """Returns a recipe"""

    recipe = Recipe(name=name, user=user)

    db.session.add(recipe)
    db.session.commit()

    return recipe


def get_recipes():
    """Returns all recipes in database"""

    """IN USE"""

    return Recipe.query.all()


def get_recipe_by_id(recipe_id):
    """Returns a specific recipe by id"""

    """IN USE"""

    return Recipe.query.get(recipe_id)



def create_ingredient(name, calories):
    """Creates an ingredient"""

    ingredient = Ingredient(name=name, calories=calories)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def get_ingredients():
    """Returns all ingredients in database"""

    """IN USE"""

    return Ingredient.query.all()


def create_recipe_ingredient(recipe, ingredient):
    """Creates relationship between a recipe and its ingredient"""

    recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient)

    db.session.add(recipe_ingredient)
    db.session.commit()

    return recipe_ingredient


def get_recipe_ingredients():
    """Returns all recipe ingredient relationships"""

    """IN USE"""

    return RecipeIngredient.query.all()


def get_recipe_ingredients_by_id(recipe_id):
    """Returns all recipe ingredient relationships"""

    """IN USE"""

    return RecipeIngredient.query.filter(RecipeIngredient.recipe_id == recipe_id).all()


def create_cleanse(start_date, end_date, public, description, user):
    """Creates a cleanse"""

    """IN USE"""

    cleanse = Cleanse(start_date=start_date, end_date=end_date, public=public, description=description, user=user)

    db.session.add(cleanse)
    db.session.commit()

    return cleanse


def get_cleanses():
    """Returns all cleanses in database"""

    """IN USE"""

    return Cleanse.query.all()


def get_cleanse_by_id(cleanse_id):
    """Returns a specific cleanse by id"""

    return Cleanse.query.get(cleanse_id)


def get_user_cleanses(user_id):
    """Returns all cleanses for a specific user"""

    """IN USE"""

    user_id = user_id

    return UserCleanse.query.filter(UserCleanse.user_id == user_id).all()


def get_user_cleanse(user_cleanse_id):
    """Returns specific user cleanse for a user"""

    """IN USE"""

    user_cleanse_id = user_cleanse_id

    return UserCleanse.query.filter(UserCleanse.user_cleanse_id == user_cleanse_id).first()


def create_user_cleanse(active, completed, cleanse, user):
    """Creates relationship between a user and their cleanse"""

    """IN USE"""

    user_cleanse = UserCleanse(active=active, completed=completed, cleanse=cleanse, user=user)

    db.session.add(user_cleanse)
    db.session.commit()

    return user_cleanse


def create_user_cleanse_recipe(timestamp, date, user_cleanse, recipe):
    """Creates relationship between a users cleanse and a recipe"""

    """IN USE"""

    user_cleanse_recipe = UserCleanseRecipe(timestamp=timestamp, date=date, user_cleanse=user_cleanse, recipe=recipe)

    db.session.add(user_cleanse_recipe)
    db.session.commit()

    return user_cleanse_recipe

def get_user_cleanse_recipes(user_cleanse_id):
    """Shows all recipes for a specific cleanse"""

    
    return UserCleanseRecipe.query.filter(UserCleanseRecipe.user_cleanse_id == user_cleanse_id).all()
        

def create_cleanse_log(timestamp, comment, private, user_cleanse):
    """Creates a comment related to a users specific cleanse"""

    cleanse_log = CleanseLog(timestamp=timestamp, comment=comment, private=private, user_cleanse=user_cleanse)

    db.session.add(cleanse_log)
    db.session.commit()

    return cleanse_log


def get_cleanse_logs(user_cleanse_id):
    """Shows all cleanse logs for a specific user cleanse"""


    return CleanseLog.query.filter(CleanseLog.user_cleanse_id == user_cleanse_id).all()



def create_global_comment(global_comment):
    """Creates a comment"""

    global_comment = GlobalComment(global_comment=global_comment)

    db.session.add(global_comment)
    db.session.commit()

    return global_comment



def get_global_comments():
    """Returns all global comments"""

    return GlobalComment.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
