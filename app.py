from flask import Flask,render_template,redirect,url_for,request,Blueprint
from dotenv import load_dotenv
import os
from db import get_db_connection,fetch_all,fetch_one,execute
load_dotenv()
from routes.Airports import Airports_bp
from routes.Airlines import Airlines_bp
from routes.Aircrafts import Aircrafts_bp

app=Flask(__name__)

app.register_blueprint(Airports_bp)
app.register_blueprint(Airlines_bp)
app.register_blueprint(Aircrafts_bp)

app.secret_key=os.getenv('SECRET_KEY','fallback_secret_for_testing')


@app.route('/')
def test_home():
    return  render_template('base.html')


if __name__=="__main__":
    app.run(debug=True)