from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx'

mongo = PyMongo(app)
api = Api(app)

class newsDataAll(Resource):
    def get(self):
        try:
            query = {}
            projection = {'_id':False}
            newsAllData = mongo.db.historyday.find(query, projection)
            listData = []
            for element in newsAllData:
                listData.append(element)
            return jsonify(listData)
        except:
            return 'Not found'

api.add_resource(newsDataAll, '/')

if __name__ == '__main__':
    app.run(debug=True)