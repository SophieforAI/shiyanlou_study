# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient
import pandas as pd


def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests =pd.DataFrame(list(db.contests.find()))
    contests_group = contests.groupby(['user_id'],as_index=False).sum()
    contests_group_sort = contests_group.sort_values(by=['score','submit_time'],ascending=[False,True])
    contests_group_sort['rank']=list(range(1,len(contests_group_sort)+1))
    user_information =  contests_group_sort[contests_group_sort['user_id']==user_id]
    score = int(user_information['score'])
    submit_time = int(user_information['submit_time'])
    rank = int(user_information['rank'])
    return rank,score,submit_time
                                

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
        print(get_rank(user_id))
    except:
        print("Parameter Error")
