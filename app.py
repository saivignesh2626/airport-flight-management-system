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

@app.route('/UpdateAirline/<int:id>',methods=['GET','POST'])
def Update_Airline(id):
    if request.method == 'POST':
        Airline_Name = request.form['Airline_Name']
        IATA_Code = request.form['IATA_Code']
        ICAO_Code = request.form['ICAO_Code']
        Airline_Country = request.form['Airline_Country']

        # The SQL UPDATE command
        sql = 'UPDATE Airline SET Name=%s, IATA_Code=%s, ICAO_Code=%s, Country=%s WHERE Airline_ID=%s'
        params = (Airline_Name, IATA_Code, ICAO_Code, Airline_Country, id)
        execute(sql, params)

        return redirect(url_for('DisplayAirline'))
    else:
        sql = 'SELECT * FROM Airline WHERE Airline_ID=%s'
        params = (id,)
        airline_to_edit = fetch_one(sql, params)
        return render_template('UpdateAirline.html', airline=airline_to_edit)
    
    
    
    
@app.route('/Airport')
def DisplayAirport():
    sql='Select *from Airport'
    Airport_Data=fetch_all(sql)
    return render_template('Airport.html',Airport_Data=Airport_Data)

@app.route('/AddAirport',methods=['POST'])
def Add_Airport():
    Airport_ID=request.form['Airport_ID']
    Airport_IATA_Code=request.form['Airport_IATA_Code']
    Airport_Name=request.form['Airport_Name']
    Airport_City=request.form['Airport_City']
    Airport_Country=request.form['Airport_Country']
    
    sql='insert into airport (Airport_ID, IATA_Code, Airport_Name, Airport_City, Airport_Country)  values (%s,%s,%s,%s,%s)'
    params=(Airport_ID,Airport_IATA_Code,Airport_Name,Airport_City,Airport_Country)
    
    execute(sql,params)
    return redirect(url_for('DisplayAirport'))


@app.route('/DeleteAirport/<int:id>',methods=['POST'])
def DeleteAirport(id):
    sql='delete from Airport where Airport_ID = %s'
    params=(id,)
    execute(sql,params)
    return redirect(url_for('DisplayAirport'))
    

@app.route('/DisplayTerminal')
def Display_Terminal():
    sql='select * from Terminal'
    Terminal_Data=fetch_all(sql)
    return render_template('Terminal.html',Terminal_Data=Terminal_Data)

@app.route('/DeleteTerminal/<int:id>',methods=['POST'])
def Delete_Terminal(id):
    sql='delete from Terminal where Terminal_ID=%s'
    params=(id,)
    execute(sql,params)
    return redirect(url_for('Display_Terminal'))


if __name__=="__main__":
    app.run(debug=True)