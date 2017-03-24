# -*- encoding: utf-8 -*-
import requests
import os
import json
import pandas as pd
import pprint
from pymongo import MongoClient

# Define the MongoDB database and table
DB_CLIENT = MongoClient('mongodb://localhost:27017/')
DB = DB_CLIENT['yummly']
COLL = DB['recipes']

USERNAME = os.environ['yum_username']
PASSWORD = os.environ['yum_password']
HEADERS = {'X-Yummly-App-ID':USERNAME,'X-Yummly-App-Key':PASSWORD, 'Accept-Encoding': None}

def make_yumly_request(params):
    '''
    Takes parameters created by chunk_recipes and gets recipe result "page"
    '''
    url = 'http://api.yummly.com/v1/api/recipes'
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

    # pprint.pprint(len(j['matches']))
    # pprint.pprint(j['totalMatchCount']) # 1602903

def chunk_recipes():
    '''
    Get recipe data from api and insert into mongodb
    in chunks of 100.
    '''
    counter = 0
    max_result = 100
    start = 1
    params = {'maxResult': max_result, 'start': start}
    # make first request to check match count number
    r = make_yumly_request(params)
    match_count =  r['totalMatchCount'] #1602903 #16101

    # insert batches of 100 results into mongodb
    while start < (match_count / max_result):
        m = make_yumly_request(params)
        COLL.insert_many(m['matches'])
        # increment the start parameter to get next "page"
        start += max_result
        counter += 1

if __name__ == '__main__':
    chunk_recipes()
