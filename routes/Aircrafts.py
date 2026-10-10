from flask import Blueprint,render_template,redirect,request,url_for
from db import get_db_connection,fetch_all,fetch_one,execute

Aircrafts_bp=Blueprint(
    'Aircrafts',
    __name__,
    url_prefix='/Aircraft'
)


@Aircrafts_bp.route('/')
def Display_Aircraft():
    sql='Select Aircraft_ID,Tail_Number,Model,Capacity,a.Airline_ID,Name as Airline_Name\
        from Aircraft a\
        join Airline al on\
        a.Airline_ID=al.Airline_ID\
        order by(Aircraft_ID)'
    Aircraft_Data=fetch_all(sql)
    Airline_Data=fetch_all('select Name,Airline_ID from Airline')
    return render_template('Aircraft.html',Aircraft_Data=Aircraft_Data,Airline_Data=Airline_Data)


@Aircrafts_bp.route('/add',methods=['POST'])
def Add_Aircraft():
    Tail_Number=request.form['Tail_Number']
    Model=request.form['Model']
    Capacity=request.form['Capacity']
    Airline_ID=request.form['Airline_ID']

    params=(Tail_Number,Model,Capacity,Airline_ID)
    sql='insert into Aircraft (Tail_Number,Model,Capacity,Airline_ID) values (%s,%s,%s,%s)'
    execute(sql,params)

    return redirect(url_for('Aircrafts.Display_Aircraft'))

