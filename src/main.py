from flask import Flask, request
import json
import sqlite3

app = Flask(__name__)

# {
	# "start": "10:00",
	# "end": "12:00",
	# "room": 123,
	# "indeks": 209433	
# }
@app.route('/make_reservation', methods = ['POST'])
def make_reservation():
	booking = request.json
	conn = sqlite3.connect('../db/bookingsDB')
	c = conn.cursor()
	c.execute('INSERT INTO bookings VALUES ({},{},{},{})'.format(booking['indeks'],
																		booking['room'],
																		booking['start'],
																	booking['end']))
	conn.commit()	
	conn.close()
	return 'OK', 200

@app.route('/', methods = ['GET'])
def hello():
	return '<h1> Hej, mordeczki!</h1>'

if __name__ == '__main__':
	print 'hehe'
	app.run()