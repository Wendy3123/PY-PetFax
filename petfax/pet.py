from flask import (Blueprint, render_template)
import json


pets = json.load(open('pets.json'))
bp = Blueprint('pet',__name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html',pets=pets)


@bp.route('<int:pet_id>')
def specificID(pet_id):
    pet = pets[pet_id-1]
    return render_template('pet.html' , pet = pet)

@bp.route('/new')
def form():
    return render_template('form.html' )