from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story_dictionary

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Default story

@app.get("/home")
def choose_story():
    """Add docstring"""
    return render_template('home.html', stories=story_dictionary)


@app.get("/questions")
def create_form():
    """ Returns form with prompts/text fields for each word needed to generate
        the story

    """
    story_name = request.args["chosen_story"]
    chosen_story = story_dictionary.get(story_name)
    return render_template('questions.html', words=chosen_story.prompts, story_name=story_name)


@app.get("/results/<story_name>")
def generate_story(story_name):
    """ Gets users words from page and returns story text with words filled in

    """
    chosen_story = story_dictionary[story_name]
    story_text = chosen_story.generate(request.args)
    return render_template('story.html', story_text=story_text)


@app.get("/add_story")
def make_story():
    """doc string"""
    return render_template('add-story.html')


@app.post("/home")
def create_new_story():
    num_nouns = request.form['number_of_nouns']
    num_verbs = request.form['number_of_verbs']
    num_adjs = request.form['number_of_adjectives']
    num_p_nouns = request.form['number_of_plural_nouns']

    words = []

    #for num in num_nouns:
    #    words.append({{noun{num}})