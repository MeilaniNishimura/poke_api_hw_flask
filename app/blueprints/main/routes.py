from flask import render_template, request, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import current_user
from app import db

@app.route("/")
def home():
    pokemons = Pokemon.query.all()

    context = {
        "pokemons": pokemons,


    }



    return render_template("home.html", **context)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pokedex")
def pokedex():
    user_pokes= current_user.pokes
    context = {
        'pokemons': user_pokes,

    }
    return render_template("pokedex.html", **context)

@app.route("/add", methods=['POST'])
def add():
    entered_pokemon = Pokemon.query.filter_by(id=request.form.get('pokemon')).first()
    entered_pokemon.user_id = current_user.id
    db.session.commit()
    return redirect(url_for('main.pokedex'))