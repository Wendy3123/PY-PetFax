from flask import Flask
app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello this is PetFax'


@app.route('/pets')
def pets():
    return 'Here are some of our pets up for adoption!'