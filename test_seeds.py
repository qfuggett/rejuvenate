"""Script to seed database."""

import os
from datetime import datetime

import crud
import model
import server

os.system('dropdb rejuvenate')
os.system('createdb rejuvenate')

model.connect_to_db(server.app)
model.db.create_all()


SEED = {
    'Tesa': {
        'info': {
            'username': 'Tesa',
            'email': 'tesa@test.com',
            'password': 'test'
        },
        'cleanse': {
            'description': 'my first cleanse!',
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.now(),
            'comment': 'it hass only been an hour and i am ready to eat',
            'private': True

        },
        'recipe': {
            'name': 'sunshine',
            'timestamp': datetime.now()
        },
        'ingredients': {
            1: {
                'name': 'orange',
                'calories': 15
            }, 
            2: {
                'name': 'banana',
                'calories': 45
            },
            3: {
                'name': 'grapefruit',
                'calories': 30
            }
        },
    },
    'Danielle': {
        'info': {
            'username': 'dhooper',
            'email': 'danielle@test.com',
            'password': 'test',
            'name': 'Danielle'
        },
        'cleanse': {
            'description': 'my first cleanse with the family!',
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.now(),
            'comment': 'im not sure if i can make it',
            'private': True

        },
        'recipe': {
            'name': 'blue storm',
            'timestamp': datetime.now()
        },
        'ingredients': {
            1: {
                'name': 'blueberries',
                'calories': 10
            }, 
            2: {
                'name': 'blackberries',
                'calories': 10
            },
            3: {
                'name': 'peaches',
                'calories': 45
            }
        },
    },
    'NyJai': {
        'info': {
            'username': 'NyJai',
            'email': 'nyjai@test.com',
            'password': 'test'
        },
        'cleanse': {
            'description': 'lets goooo',
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.now(),
            'comment': 'im confident!',
            'private': True

        },
        'recipe': {
            'name': 'plain',
            'timestamp': datetime.now()
        },
        'ingredients': {
            1: {
                'name': 'apples',
                'calories': 65
            }, 
            2: {
                'name': 'banana',
                'calories': 45
            },
            3: {
                'name': 'almond milk',
                'calories': 100
            }
        },
    },
    'Linda': {
        'info': {
            'username': 'absrlife',
            'email': 'linda@test.com',
            'password': 'test'
        },
        'cleanse': {
            'description': 'first cleanse of the week!',
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.now(),
            'comment': 'im feeling great',
            'private': True

        },
        'recipe': {
            'name': 'vampire',
            'timestamp': datetime.now()
        },
        'ingredients': {
            1: {
                'name': 'pomegranate juice',
                'calories': 65
            }, 
            2: {
                'name': 'cherries',
                'calories': 45
            },
            3: {
                'name': 'tomato',
                'calories': 30
            }
        },
    },
    'Marcie': {
        'info': {
            'username': 'marcie',
            'email': 'marcie@test.com',
            'password': 'test'
        },
        'cleanse': {
            'description': 'first cleanse ever!',
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.now(),
            'comment': 'we will see how this goes',
            'private': True

        },
        'recipe': {
            'name': 'veggie bomb',
            'timestamp': datetime.now()
        },
        'ingredients': {
            1: {
                'name': 'kale',
                'calories': 25
            }, 
            2: {
                'name': 'spinach',
                'calories': 35
            },
            3: {
                'name': 'almond milk',
                'calories': 100
            }
        },
    }
}

for i in SEED:
    username = SEED[i]['info']['username']
    email = SEED[i]['info']['email']
    password = SEED[i]['info']['password']

    description = SEED[i]['cleanse']['description']
    start_date = SEED[i]['cleanse']['start_date']
    end_date = SEED[i]['cleanse']['end_date']
    public = SEED[i]['cleanse']['public']
    active = SEED[i]['cleanse']['active']
    completed = SEED[i]['cleanse']['completed']

    clog_timestamp = SEED[i]['cleanse_log']['timestamp']
    comment = SEED[i]['cleanse_log']['comment']
    private = SEED[i]['cleanse_log']['private']

    r_name = SEED[i]['recipe']['name']
    timestamp = SEED[i]['recipe']['timestamp']
    

    i_name = SEED[i]['ingredients'][1]['name']
    calories = SEED[i]['ingredients'][1]['calories']
    i_name_2 = SEED[i]['ingredients'][2]['name']
    calories_2 = SEED[i]['ingredients'][2]['calories']
    i_name_3 = SEED[i]['ingredients'][3]['name']
    calories_3 = SEED[i]['ingredients'][3]['calories']




    db_user = crud.create_user(username, email, password)
    db_ingredient = crud.create_ingredient(i_name, calories)
    db_ingredient_2 = crud.create_ingredient(i_name_2, calories_2)
    db_ingredient_3 = crud.create_ingredient(i_name_3, calories_3)
    db_recipe = crud.create_recipe(r_name, db_user)
    db_cleanse = crud.create_cleanse(start_date, end_date, public, description, db_user)

    crud.create_recipe_ingredient(db_recipe, db_ingredient)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_2)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_3)

    db_user_cleanse = crud.create_user_cleanse(active, completed, db_cleanse, db_user)
    crud.create_user_cleanse_recipe(timestamp, start_date, db_user_cleanse, db_recipe)
    crud.create_cleanse_log(clog_timestamp, comment, private, db_user_cleanse)