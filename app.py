from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/questions")
def create_form():
    """ Returns form with prompts/text fields for each word needed to generate
        the story

    """
    return render_template('questions.html', words=silly_story.prompts)


@app.get("/results")
def generate_story():
    """ Gets users words from page and returns story text with words filled in

    """
    story_text = silly_story.generate(request.args)
    return render_template('story.html', story_text=story_text)