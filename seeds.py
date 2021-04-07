"""Script to seed database."""

import os
import json
from random import choice, randint
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
            'password': 'test',
            'name': 'QueenTesa'
        },
        'cleanse': {
            'description': 'my first cleanse!',
            'start_date': datetime.now(),
            'end_date': '',
            'public': FALSE,
            'active': TRUE,
            'completed': FALSE
        },
        'cleanse_log': {
            'timestamp': datetime.now().time(),
            'comment': 'it hass only been an hour and i am ready to eat',
            'private': TRUE

        },
        'recipe': {
            'name': 'sunshine',
            'timestamp': datetime.now().time()
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
    # 'Danielle': {},
    # 'NyJai': {},
    # 'Linda': {},
    # 'Marcie': {}
}

for i in SEED:
    username = SEED[i]['info']['username']
    email = SEED[i]['info']['email']
    password = SEED[i]['info']['password']
    name = SEED[i]['info']['username']

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



    db_user = crud.create_user(username, email, password, name)
    db_ingredient = crud.create_ingredient(i_name, calories)
    db_recipe = crud.create_recipe(r_name, db_user)
    db_cleanse = crud.create_cleanse(start_date, end_date, public, description, db_user)

    crud.create_recipe_ingredient(db_recipe, db_ingredient)
    db_user_cleanse = crud.create_user_cleanse(active, completed, db_cleanse, db_user)
    crud.create_user_cleanse_recipe(timestamp, start_date, db_user_cleanse, db_recipe)
    crud.create_cleanse_log(clog_timestamp, comment, private, db_user_cleanse)

