from flask import Flask,render_template,redirect,url_for,request
from dotenv import load_dotenv
import os
from db import get_db_connection,fetch_all,fetch_one,execute
load_dotenv()

app=Flask(__name__)

app.secret_key=os.getenv('SECRET_KEY','fallback_secret_for_testing')


@app.route('/')
def test_home():
    return "testing the app.py"

@app.route('/Airline')
def DisplayAirline():
    Airline_Data=fetch_all('select * from Airline')
    return render_template('Airline.html',Airline_Data=Airline_Data)


@app.route('/AddAirline',methods=['POST'])
def Add_Airline():
    Airline_Name=request.form['Airline_Name']
    IATA_Code=request.form['IATA_Code']
    ICAO_Code=request.form['ICAO_Code']
    Airline_Country=request.form['Airline_Country']

    params=(Airline_Name,IATA_Code,ICAO_Code,Airline_Country)
    sql='insert into Airline (Name,IATA_Code,ICAO_Code,Country) values (%s,%s,%s,%s)'
    execute(sql,params)

    return redirect(url_for('DisplayAirline'))


@app.route('/DeleteAirline/<int:id>',methods=['POST'])
def Delete_Airline(id):
    params=(id,)
    sql='Delete from Airline Where Airline_ID=%s'
    execute(sql,params)
    return redirect(url_for('DisplayAirline'))



if __name__=="__main__":
    app.run(debug=True)