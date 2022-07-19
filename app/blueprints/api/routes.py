from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Pokemon
from app import db



@app.route("/create_pokemon", methods=["POST"])
def create_pokemon():
    user = 1

    name = request.form['name']
    description = request.form['description']
    type = request.form['type']

    new_pokemon = Pokemon(name=name, description=description, type=type)
    db.session.add(new_pokemon)
    db.session.commit()

    return redirect("http://127.0.0.1:5000/")