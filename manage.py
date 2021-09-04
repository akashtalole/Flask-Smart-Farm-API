from flask import Flask
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('Farm', description='Flask Smart Farm APIs')
land_name_space = app.namespace('Land', description='Land APIs')
farmer_name_space = app.namespace('Farmer', description='Farmer APIs')
crop_name_space = app.namespace('Crop', description='Crop APIs')


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
	def put(self):
		return {
			"status": "Updated data"
		}
	def delete(self):
		return {
			"status": "Deleted data"
		}

@land_name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Get land data"
		}
	def post(self):
		return {
			"status": "Posted land data"
		}
	def put(self):
		return {
			"status": "Updated land data"
		}
	def delete(self):
		return {
			"status": "Deleted land data"
		}
@farmer_name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Get farmer data"
		}
	def post(self):
		return {
			"status": "Posted farmer data"
		}
	def put(self):
		return {
			"status": "Updated farmer data"
		}
	def delete(self):
		return {
			"status": "Deleted farmer data"
		}
@crop_name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Get crop data"
		}
	def post(self):
		return {
			"status": "Posted crop data"
		}
	def put(self):
		return {
			"status": "Updated crop data"
		}
	def delete(self):
		return {
			"status": "Deleted crop data"
		}
if __name__ == '__main__':
	flask_app.run(host="0.0.0.0", debug=True)