from flask import Flask,render_template,request,redirect
from models import db,TripModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        trip_info = request.form['trip_info']
        name = request.form['name']
        length = request.form['length']
        location = request.form['location']
        trip = TripModel(trip_info=trip_info, name=name, length=length, location = location)
        db.session.add(trip)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    trips = TripModel.query.all()
    return render_template('datalist.html',trips = trips)
 
 
@app.route('/data/<int:id>')
def RetrieveTrip(id):
    trip = TripModel.query.filter_by(trip_info=id).first()
    if trip:
        return render_template('data.html', trip = trip)
    return f"Trip info ={id} does not exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    trip = TripModel.query.filter_by(trip_info=id).first()
    if request.method == 'POST':
        if trip:
            db.session.delete(trip)
            db.session.commit()
            name = request.form['name']
            length = request.form['length']
            location = request.form['location']
            trip = TripModel(trip_info=id, name=name, length=length, location = location)
            db.session.add(trip)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Trip info ={id} does not exist"
 
    return render_template('update.html', trip = trip)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    trip = TripModel.query.filter_by(trip_info=id).first()
    if request.method == 'POST':
        if trip:
            db.session.delete(trip)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='localhost', port=5000)