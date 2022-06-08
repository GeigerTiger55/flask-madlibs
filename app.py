from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

STORIES = {"silly": silly_story, "excited": excited_story}

# Default story

@app.get("/home")
def choose_story():

    return render_template('home.html', stories=STORIES)

@app.get("/questions")
def create_form():
    """ Returns form with prompts/text fields for each word needed to generate
        the story

    """
    global chosen_story
    chosen_story = STORIES.get(request.args["chosen_story"])
    return render_template('questions.html', words=chosen_story.prompts)

@app.get("/results")
def generate_story():
    """ Gets users words from page and returns story text with words filled in

    """
    story_text = chosen_story.generate(request.args)
    return render_template('story.html', story_text=story_text)