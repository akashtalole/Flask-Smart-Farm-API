from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_sqlalchemy import SQLAlchemy
#from flask_restplus_patched import Api, Namespace, Resource, ModelSchema


flask_app = Flask(__name__)
db = SQLAlchemy(flask_app)
app = Api(app = flask_app)

#app = Api(flask_app)

name_space = app.namespace('Farm', description='Flask Smart Farm APIs')
land_name_space = app.namespace('Land', description='Land APIs')
farmer_name_space = app.namespace('Farmer', description='Farmer APIs')
crop_name_space = app.namespace('Crop', description='Crop APIs')
livestock_space = app.namespace('Livestock', description='Livestock management')
activities_space = app.namespace('Activities', description='Activities management')
prices_space = app.namespace('Prices', description='Crop Prices')
fertilizers_space = app.namespace('Fertilizers', description='Fertilizers')
precision_farming_space = app.namespace('Precesion Farming', description='Precesion Farming')

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

@livestock_space.route("/")
class MainClass(Resource):
	def get(self):
		return { "status": "Get livestock data"}
	
	def post(self):
		return { "status": "Add livestock data"}

	def put(self):
		return { "status": "Update livestock data"}

	def delete(self):
		return { "status": "delete livestock data"}

@activities_space.route("/")
class MainClass(Resource):
	def get(self):
		return { "status": "Get Activity data"}
	
	def post(self):
		return { "status": "Add Activity data"}

	def put(self):
		return { "status": "Update Activity data"}

	def delete(self):
		return { "status": "delete Activity data"}

@prices_space.route("/")
class MainClass(Resource):
	def get(self):
		return { "status": "Get Prices data"}
	
	def post(self):
		return { "status": "Add Prices data"}

	def put(self):
		return { "status": "Update Prices data"}

	def delete(self):
		return { "status": "delete Prices data"}

@fertilizers_space.route("/")
class MainClass(Resource):
	def get(self):
		return { "status": "Get fertilizers data"}
	
	def post(self):
		return { "status": "Add fertilizers data"}

	def put(self):
		return { "status": "Update fertilizers data"}

	def delete(self):
		return { "status": "delete fertilizers data"}

@precision_farming_space.route("/")
class MainClass(Resource):
	def get(self):
		return { "status": "Get Precesion Farming data"}
	
	def post(self):
		return { "status": "Add Precesion Farming data"}

	def put(self):
		return { "status": "Update Precesion Farming data"}

	def delete(self):
		return { "status": "delete Precesion Farming data"}

if __name__ == '__main__':
	flask_app.run(host="0.0.0.0", debug=True)
