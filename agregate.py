from bson.son import SON
import pymongo
import bottle
# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")
i = 0
db = connection.students  # attach to db
collection = db.grades  # specify the colllection
q = collection.find({"type": "homework"})
q = q.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
delArray = {}
for row in q:
    delArray[row['student_id']] = {"id": row['_id'], "score": row['score']}

# for delRow in delArray:
    # collection.remove({"_id": delArray[delRow]['id']})