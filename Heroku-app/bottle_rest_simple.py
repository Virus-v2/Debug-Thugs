from bottle import run, get, post, request, delete, default_app
import model
import pickle

# @get('/location')
# def getAll():
# 	#insert_db()
# 	return {'location' : database.myrecords()}

# 	#database.clear()

# @get('/clear/delete/db')
# def clear_DB():
# 	database.clear()

#loading the model
loaded_model = pickle.load(open('model_svm.pkl', 'rb'))

@post('/data')
def process():	
	#model.show(request.json)
	model.predictPotholes(request.json)
	#print(type(request.json))
	#return str

app = default_app()


#following for normal bottle app
#run(host = '0.0.0.0', reloader=True, server = 'gunicorn', debug=True, workers=4)

# to run a post request use following
# r = requests.post('http://localhost:8080/animal', json = dt)
