from flask import Flask, render_template
# , request, redirect, flash
from restaurants import berkeley_restaurant_week
import os
import random

app = Flask(__name__)
app.secret_key = 'Iamsoooooooohungry'


@app.route('/')
def home():
    """This is the restaurant picker home page"""
    # give the user the home page, which has a form to set filters.
    return render_template("home.html")


@app.route('/whats_for_tonight')
def pick_random():
    """this is the 'action' after user click 'random pick' button.
       It randomly picks a restaurant and shows its details."""

    candidates = berkeley_restaurant_week.keys()
    winner = random.choice(candidates)
    details = berkeley_restaurant_week.get(winner)

    return render_template("whats_for_tonight.html", details=details)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
