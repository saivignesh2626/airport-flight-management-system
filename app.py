from flask import Flask,render_template,redirect
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__)

app.secret_key=os.getenv('SECRET_KEY','fallback_secret_for_testing')


@app.route('/')
def test_home():
    return "testing the app.py"


if __name__=="__main__":
    app.run(debug=True)