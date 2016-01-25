from flask import Flask, render_template, flash
# , request, redirect
# from restaurants import berkeley_restaurant_week
import os

app = Flask(__name__)
app.secret_key = 'Iamsoooooooohungry'


@app.route("/")
def home():
    """This is the restaurant picker home page"""
    # give the user the home page, which has a form to set filters.
    return render_template("home.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
