from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx'

mongo = PyMongo(app)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('date', type=str)
parser.add_argument('category', type=str)

class categoryData(Resource):
    def get(self):
        
        args = parser.parse_args()
    
        categoryData = args['category']
        dateData = args['date']

        # try:
        # query = {"categoryData": category(categoryData)}
        # query พร้อมกัน
        # query = {'category': categoryData,'time':dateData}
        # query เเบบเดียว
        if categoryData and dateData:
            query = {'category': categoryData,'time':dateData}
        elif categoryData:
            query = {'category': categoryData}
        elif dateData:
            query = {'time': dateData}
       
        projection = {'_id':False}

        categoryDataAll = mongo.db.news.find(query, projection)
    
        return jsonify(list(categoryDataAll))
    # http://127.0.0.1:5000/news?category=travel&date=2019-01-10 <== ดูได้
    # http://127.0.0.1:5000/news?category=travel
    # http://127.0.0.1:5000/news?date=2019-01-09
        # except:
        #     return 'Not found'

class newsDataAll(Resource):
    def get(self):
        try:
            query = {}
            projection = {'_id':False}
            newsAllData = mongo.db.news.find(query, projection)
            listData = []
            for element in newsAllData:
                listData.append(element)
            return jsonify(listData)
        except:
            return 'Not found'

api.add_resource(newsDataAll, '/')
api.add_resource(categoryData, '/news')

if __name__ == '__main__':
    app.run(debug=True)