from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import json

from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx'

mongo = PyMongo(app)
api = Api(app)
# parser = reqparse.RequestParser()
# parser.add_argument('category', type=str)

def category(category):
    categoryAll = category[0:2]
    categoryList = {
      "01": "technology",
    }
    if categoryAll in categoryList:
        return categoryList[categoryAll]

class categoryData(Resource):
    def get(self):
        # calendar = date(date)
        # args = parser.parse_args()
        # categoryData = args['category']
        # เอาค่ามาเก็บในcalendar
        # return "Input is {}".format(date(calendar))
        try:
        # เอาจากdatabaseเราซื่อcontentDataเทียบกับฟังชั้น
            # query = {"categoryData": category(categoryData)}
            # projection = {'_id':False}
            # categoryDataAll = mongo.db.news.find(query, projection)
            # return jsonify(categoryDataAll[0])
            return 'xsdsf'
        except:
            return 'Not found'

# class newsDataAll(Resource):
#     def get(self):
#         try:
#             query = {}
#             projection = {'_id':False}
#             newsAllData = mongo.db.news.find(query, projection)
#             listData = []
#             for element in newsAllData:
#                 listData.append(element)
#             return jsonify(listData)
#         except:
#             return 'Not found'

# api.add_resource(newsDataAll, '/')
api.add_resource(categoryData, '/category', )
if __name__ == '__main__':
    app.run(debug=True)