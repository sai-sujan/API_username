from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pyrebase
import os

app = Flask(__name__)
# for '/' route return name app
@app.route('/')
def index():
    return "API to retrieve username"
#get_item_list using flask
@app.route('/api1', methods=['GET'])
def get_item_list():
    color = request.args.get('color')
    food = request.args.get('food')
    movie = request.args.get('movie')
    pet = request.args.get('pet')
    sport = request.args.get('sport')
    firebaseConfig = {
        "apiKey": "AIzaSyD-2iQRWn7utb78q3MYboKn5xnumKFbbc0",
        "authDomain": "login-check-grootan.firebaseapp.com",
        "databaseURL": "https://login-check-grootan-default-rtdb.firebaseio.com",
        "projectId": "login-check-grootan",
        "storageBucket": "login-check-grootan.appspot.com",
        "messagingSenderId": "90726747758",
        "appId": "1:90726747758:web:ad07c4e9c419518ab1607f",
        "measurementId": "G-W8RDFH3RZE"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    dict = {"color": color, "food": food, "movie": movie, "pet": pet, "sport": sport}
    for i in db.child("Autentication").get():
        if (i.val() == dict):
            return ({'username': i.key()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)