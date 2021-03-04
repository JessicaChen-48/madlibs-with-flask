from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)

@app.route("/")
def home():

    # pass in prompts list to questions.html
    all_prompts = silly_story.prompts

    return render_template(
        "questions.html",
        prompts=all_prompts)

@app.route("/story")
def generate_story():

    # for each prompt, add a key-value pair into answers dictionary
    all_prompts = silly_story.prompts

    answer = {}
    for prompt in all_prompts:
        answer[prompt] = request.args.get(prompt)


    # generate silly story, passing the entire story as a parameter to story.html
    story = silly_story.generate(answer)

    return render_template("story.html",
    story = story)