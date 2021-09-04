from flask import Flask
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('Farm', description='Flask Smart Farm APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

if __name__ == '__main__':
	flask_app.run(host="0.0.0.0", debug=True)