from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pyrebase
import os

app = Flask(__name__)
# for '/' route return name app

#get_item_list using flask

@app.route('/api', methods=['GET','POST'])
def get_questions_and_answers():

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
    ques = db.child("checking").get()
    for i in ques.each():
        questions_dict = i.val()
        questions = list(questions_dict.keys())
        answers = list(questions_dict.values())
    # generate 5 non repetative random numbers between 1 to 10

        import random

        random_list = []
        while len(random_list) < 5:
            random_number = random.randint(0, 9)
            if random_number not in random_list:
                random_list.append(random_number)


        numberList = random_list

        q=[]
        a=[]
        for i in random_list:

                q.append(questions[i])
                a.append(answers[i])


        result = dict(zip(q, a))
        return result


if __name__ == '__main__':
    #app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
