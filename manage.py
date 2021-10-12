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
loan_space = app.namespace('Loan Management', description='Loan Management')
credit_space = app.namespace('Credit Management', description='Credit Management')
seed_space = app.namespace('Seed Management', description='Seed Management')
equipment_space = app.namespace('Equipment Management', description='Equipment Management')
soiltesting_space = app.namespace('Soil Testing', description='Soil Testing')
insurance_space = app.namespace('Insurance', description='Insurance')
pesticide_space = app.namespace('Pesticide management', description='Pesticide')
landrecord_space = app.namespace('Land Record', description='Land Record')
apmc_space = app.namespace('APMC Data', description='APMC')
erigation_space = app.namespace('Erigation Management', description="Erigation")

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

@loan_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get Farming loan data"}
	
	def post(self):
		return { "status": "Add Farming loan data"}

	def put(self):
		return { "status": "Update Farming loan data"}

	def delete(self):
		return { "status": "Delete Farming loan data"}

@credit_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get Credit data"}
	
	def post(self):
		return { "status": "Add credit data"}

	def put(self):
		return { "status": "Update credit data"}

	def delete(self):
		return { "status": "Delete Credit data"}

@seed_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get Seed data"}
	
	def post(self):
		return { "status": "Add Seed data"}

	def put(self):
		return { "status": "Update Seed data"}

	def delete(self):
		return { "status": "Delete Seed data"}

@equipment_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get equipment data"}
	
	def post(self):
		return { "status": "Add equipment  data"}

	def put(self):
		return { "status": "Update equipment data"}

	def delete(self):
		return { "status": "Delete equipment data"}

@soiltesting_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get soil testing data"}
	
	def post(self):
		return { "status": "Add soil testing data"}

	def put(self):
		return { "status": "Update soil testing data"}

	def delete(self):
		return { "status": "Delete soil testing data"}

@insurance_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get insurance data"}
	
	def post(self):
		return { "status": "Add insurance data"}

	def put(self):
		return { "status": "Update insurance data"}

	def delete(self):
		return { "status": "Delete insurance data"}

@pesticide_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get pesticide data"}
	
	def post(self):
		return { "status": "Add pesticide data"}

	def put(self):
		return { "status": "Update pesticide data"}

	def delete(self):
		return { "status": "Delete pesticide data"}

@landrecord_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get land record data"}
	
	def post(self):
		return { "status": "Add land record data"}

	def put(self):
		return { "status": "Update land record data"}

	def delete(self):
		return { "status": "Delete land record data"}

@apmc_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get APMC data"}
	
	def post(self):
		return { "status": "Add APMC data"}

	def put(self):
		return { "status": "Update APMC data"}

	def delete(self):
		return { "status": "Delete APMC data"}

@erigation_space.route("/")
class MainClass(Resource):

	def get(self):
		return { "status": "Get erigation data"}
	
	def post(self):
		return { "status": "Add erigation data"}

	def put(self):
		return { "status": "Update erigation data"}

	def delete(self):
		return { "status": "Delete erigation data"}
if __name__ == '__main__':
	flask_app.run(host="0.0.0.0", debug=True)
