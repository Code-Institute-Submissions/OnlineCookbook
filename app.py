import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Loads Flask and PyMongo, and loads database
app = Flask(__name__)
app.config["MONGO_DB"] = 'project-four'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


# Function that loops through a list and returns how many items are in that list in the format of a dictionary that prints the type of item and the count of that item.
def get_counts(recipes, individual_item, list_of_items):
    item_counts = [0 for i in list_of_items]
    i=0
    while i < len(list_of_items):
        j=0
        while j < len(recipes):
            item = recipes[j][str(individual_item)].lower()
            if item == list_of_items[i]:
                item_counts[i] += 1
            j += 1
        i += 1
    return dict(zip(list_of_items, item_counts))
    

# Returns the home page, which used the get_counts function to list the number of different types of recipes, so the user can drill down into their chosen categories.
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    recipes = mongo.db.recipes.find()
    cuisine_list_looped = mongo.db.cuisine_list.find()
    vegetarian_list_looped=mongo.db.vegetarian_list.find()
    author_list_looped=mongo.db.authors_list.find()
    recipe_objects = [recipe for recipe in recipes]
    
    cuisine_names = [cuisine['cuisine_name'].lower() for cuisine in cuisine_list_looped]
    cuisine_counts = get_counts(recipe_objects, 'cuisine_name', cuisine_names)
    
    authors_names = [auth['author'].lower() for auth in author_list_looped]
    author_counts = get_counts(recipe_objects, 'author_name', authors_names)
        
    veg_type = [veg['vegetarian'].lower() for veg in vegetarian_list_looped]
    veg_counts = get_counts(recipe_objects, 'recipe_is_vegetarian', veg_type)
    
    return render_template("recipes.html", 
    recipes=recipes,
    cuisine_list = mongo.db.cuisine_list.find(),
    authors_list=mongo.db.authors_list.find(),
    vegetarian_list=mongo.db.vegetarian_list.find(),
    veg_counts=veg_counts,
    cuisine_counts=cuisine_counts, 
    author_counts = author_counts, 
    all_recipe_count = mongo.db.recipes.count())
    

# Function that returns all recipes from the recipes collction in the database
@app.route('/all_recipes')
def all_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("all_recipes.html",
            recipes= recipes)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)