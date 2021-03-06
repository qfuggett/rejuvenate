"""Script to seed database."""

import os
import datetime
import crud
import model
import server
import bcrypt

os.system('dropdb rejuvenate')
os.system('createdb rejuvenate')

model.connect_to_db(server.app)
model.db.create_all()


SEED = {
    'Tesa': {
        'info': {
            'username': 'Tesa',
            'email': 'qfuggett@gmail.com',
            'password': 'Hammas012',
            'name': 'Tessy',
            'location': 'Detroit, MI',
            'about': 'All you need to know is that I am excited!',
            'member_since': datetime.date(2021, 2, 21)
        },
        'cleanse': {
            'description': 'My first cleanse!',
            'start_date': datetime.date(2021, 2, 21),
            'end_date': datetime.date(2021, 2, 24),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.date(2021, 2, 21),
            'comment': 'I am so excited for smoothies!',
            'private': True

        },
        'recipe': {
            'name': 'Sunshine',
            'timestamp': datetime.date(2021, 2, 21)
        },
        'ingredients': {
            1: {
                'name': 'orange',
                'calories': 15,
                'measurement': 'whole',
                'photo': "https://www.telegraph.co.uk/multimedia/archive/01834/orange_1834038b.jpg"
            }, 
            2: {
                'name': 'banana',
                'calories': 45,
                'measurement': 'whole',
                'photo': "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg"
            },
            3: {
                'name': 'grapefruit',
                'calories': 30,
                'measurement': 'whole',
                'photo': "https://cdn.britannica.com/22/122522-050-6CD1C3E7/Grapefruit.jpg"
            }
        },
        'global_comments': {
            'comment': 'How is everyone doing?!',
            'timestamp': datetime.date(2021, 2, 21)
        }
    },
    'Danielle': {
        'info': {
            'username': 'dhooper',
            'email': 'danielle@test.com',
            'password': 'hooper',
            'name': 'Danielle',
            'location': 'Canton, MI',
            'about': 'Joined because my daughter suggested :)',
            'member_since': datetime.date(2021, 2, 21)
        },
        'cleanse': {
            'description': 'My first cleanse with the family!',
            'start_date': datetime.date(2021, 2, 22),
            'end_date': datetime.date(2021, 2, 24),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.date(2021, 2, 22),
            'comment': "Let's do this!",
            'private': True

        },
        'recipe': {
            'name': 'Blue Storm',
            'timestamp': datetime.date(2021, 2, 22)
        },
        'ingredients': {
            1: {
                'name': 'blueberries',
                'calories': 10,
                'measurement': 'cup',
                'photo': "https://cdn.oregonaitc.org/wp-content/uploads/2020/02/blueberries-690072_640-375x426.jpg"
            }, 
            2: {
                'name': 'blackberries',
                'calories': 10,
                'measurement': 'cup',
                'photo': "https://post.healthline.com/wp-content/uploads/2020/03/black-raspberries-732x549-thumbnail.jpg"
            },
            3: {
                'name': 'peaches',
                'calories': 45,
                'measurement': 'whole',
                'photo': "https://billsberryfarm.com/wp-content/uploads/2020/08/peach.png"
            }
        },
        'global_comments': {
            'comment': 'I am too!',
            'timestamp': datetime.date(2021, 2, 22)
        }
    },
    'NyJai': {
        'info': {
            'username': 'NyJai',
            'email': 'nyjai@test.com',
            'password': 'existorlive',
            'name': 'YayyYayy',
            'location': 'Southfield, MI',
            'about': 'Needed a tracker for my accountability',
            'member_since': datetime.date(2021, 3, 9)
        },
        'cleanse': {
            'description': 'Lets goooo',
            'start_date': datetime.date(2021, 3, 9),
            'end_date': datetime.date(2021, 3, 12),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.date(2021, 3, 10),
            'comment': 'Im confident!',
            'private': True

        },
        'recipe': {
            'name': 'Sweet Apple',
            'timestamp': datetime.date(2021, 3, 9)
        },
        'ingredients': {
            1: {
                'name': 'apples',
                'calories': 65,
                'measurement': 'sliced',
                'photo': "https://s3.amazonaws.com/yummy_uploads2/blog/6398.jpg"
            }, 
            2: {
                'name': 'banana',
                'calories': 45,
                'measurement': 'whole',
                'photo': "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg"
            },
            3: {
                'name': 'almond milk',
                'calories': 100,
                'measurement': 'cup',
                'photo': "https://www.dishbydish.net/wp-content/uploads/How-to-Make-Almond-Milk-Dairy-Free-Vegan_Final2-scaled.jpg"
            }
        },
        'global_comments': {
            'comment': 'I am enjoying my smoothies..are you?',
            'timestamp': datetime.date(2021, 3, 9)
        }
    },
    'Linda': {
        'info': {
            'username': 'absrlife',
            'email': 'linda@test.com',
            'password': 'flowers',
            'name': "The Cool Gma",
            'location': 'Oak Park, MI',
            'about': 'Im an expert at this!',
            'member_since': datetime.date(2021, 3, 24)
        },
        'cleanse': {
            'description': 'First cleanse of the year!',
            'start_date': datetime.date(2021, 3, 24),
            'end_date': datetime.date(2021, 3, 26),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.date(2021, 3, 24),
            'comment': 'Im feeling great',
            'private': True

        },
        'recipe': {
            'name': 'Vampire',
            'timestamp': datetime.date(2021, 3, 24)
        },
        'ingredients': {
            1: {
                'name': 'pomegranate juice',
                'calories': 65,
                'measurement': 'cup',
                'photo': "https://cdn-prod.medicalnewstoday.com/content/images/articles/318/318385/halves-pomegranate-with-seeds-and-pomegranate-juice-on-marbled-surface.jpg"
            }, 
            2: {
                'name': 'cherries',
                'calories': 45,
                'measurement': 'ounce',
                'photo': "https://images.ctfassets.net/lufu0clouua1/57roskVwfCWmgkoQW4yQmq/b90cdd9fa2f150ded98625c156358412/Red-Cherries.jpg"
            },
            3: {
                'name': 'tomato',
                'calories': 30,
                'measurement': 'whole',
                'photo': "https://media.istockphoto.com/photos/tomato-isolated-on-white-background-picture-id466175630?k=6&m=466175630&s=612x612&w=0&h=fu_mQBjGJZIliOWwCR0Vf2myRvKWyQDsymxEIi8tZ38="
            }
        },
        'global_comments': {
            'comment': 'Today is my first day',
            'timestamp': datetime.date(2021, 3, 24)
        }
    },
    'Marcie': {
        'info': {
            'username': 'marcie',
            'email': 'marcie@test.com',
            'password': 'bella',
            'name': 'Marcie',
            'location': 'Charlotte, NC',
            'about': 'New to this...but excited',
            'member_since': datetime.date(2021, 4, 1)
        },
        'cleanse': {
            'description': 'First cleanse ever!',
            'start_date': datetime.date(2021, 4, 1),
            'end_date': datetime.date(2021, 4, 3),
            'public': False,
            'active': True,
            'completed': False
        },
        'cleanse_log': {
            'timestamp': datetime.date(2021, 4, 1),
            'comment': 'We will see how this goes',
            'private': True

        },
        'recipe': {
            'name': 'Veggie bomb',
            'timestamp': datetime.date(2021, 4, 1)
        },
        'ingredients': {
            1: {
                'name': 'kale',
                'calories': 25,
                'measurement': 'ounce',
                'photo': "https://snaped.fns.usda.gov/sites/default/files/styles/crop_ratio_7_5/public/seasonal-produce/2018-05/kale.jpg?itok=Zn8Cux6F"
            }, 
            2: {
                'name': 'spinach',
                'calories': 35,
                'measurement': 'ounce',
                'photo': "https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/270609_2200-732x549.jpg"
            },
            3: {
                'name': 'almond milk',
                'calories': 100,
                'measurement': 'cup',
                'photo': "https://www.dishbydish.net/wp-content/uploads/How-to-Make-Almond-Milk-Dairy-Free-Vegan_Final2-scaled.jpg"
            }
        },
        'global_comments': {
            'comment': "I think I'm going to quit...",
            'timestamp': datetime.date(2021, 4, 1)
        }
    }
}

for i in SEED:    

    username = SEED[i]['info']['username']
    email = SEED[i]['info']['email']
    password = SEED[i]['info']['password']
    name = SEED[i]['info']['name']
    location = SEED[i]['info']['location']
    about = SEED[i]['info']['about']
    member_since = SEED[i]['info']['member_since']

    salt = bcrypt.gensalt()
    b = password.encode("utf-8")
    hashed = bcrypt.hashpw(b, salt)

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
    measurement_1 = SEED[i]['ingredients'][1]['measurement']
    photo_1 = SEED[i]['ingredients'][1]['photo']
    i_name_2 = SEED[i]['ingredients'][2]['name']
    calories_2 = SEED[i]['ingredients'][2]['calories']
    measurement_2 = SEED[i]['ingredients'][2]['measurement']
    photo_2 = SEED[i]['ingredients'][2]['photo']
    i_name_3 = SEED[i]['ingredients'][3]['name']
    calories_3 = SEED[i]['ingredients'][3]['calories']
    measurement_3 = SEED[i]['ingredients'][3]['measurement']
    photo_3 = SEED[i]['ingredients'][3]['photo']

    global_comment_dict = SEED[i].get('global_comments', {'comment': 'test'})
    global_comment = global_comment_dict['comment']
    comment_timestamp = global_comment_dict['timestamp']


    db_user = crud.create_user(username, email, hashed, name, location, about, member_since)
    db_ingredient = crud.create_ingredient(i_name, calories, measurement_1, photo_1)
    db_ingredient_2 = crud.create_ingredient(i_name_2, calories_2, measurement_2, photo_2)
    db_ingredient_3 = crud.create_ingredient(i_name_3, calories_3, measurement_3, photo_3)
    db_recipe = crud.create_recipe(r_name, db_user)
    db_cleanse = crud.create_cleanse(start_date, end_date, public, description, db_user)

    crud.create_recipe_ingredient(db_recipe, db_ingredient)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_2)
    crud.create_recipe_ingredient(db_recipe, db_ingredient_3)

    db_user_cleanse = crud.create_user_cleanse(active, completed, db_cleanse, db_user)
    crud.create_user_cleanse_recipe(timestamp, start_date, db_user_cleanse, db_recipe)
    crud.create_cleanse_log(clog_timestamp, comment, private, db_user_cleanse)

    db_comment = crud.create_global_comment(global_comment, timestamp, db_user)

