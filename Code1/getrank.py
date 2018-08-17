import sys
from pymongo import MongoClient 
from bson.son import SON

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    a = db.contests.aggregate([
        {'$group': {
            '_id': '$user_id',
            'totalscore': {'$sum': "$score"}, 
            'totaltime': {'$sum': '$submit_time'}
        }},
        {'$sort':
           SON([('totalscore', -1), ('totaltime', 1)])
        }
    ])
    for i, j  in enumerate(a):
        if j['_id'] == user_id:
            return i+1, j['totalscore'], j['totaltime']

if __name__ == '__main__':
    print(get_rank(int(sys.argv[1])))
