from facebook_page_scraper import Facebook_scraper
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
from bson.json_util import  dumps as dmps
load_dotenv()




class fb_scraper:

    @staticmethod
    def scrape_data(page_name, posts_count= 10,  browser = "firefox", proxy = "IP:PORT", timeout = 600, headless = True ):
        '''class static method to scrape data from fb'''
        meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)
        data = meta_ai.scrap_to_json()
        json_data = json.loads(data)
        return json_data
    @staticmethod
    def load_data(uri, db, collection, data_ins ):
        '''class static method to load data in mongodb'''
        conn = MongoClient(uri)
        db = conn[db]
        coll = db[collection]
        coll.insert_one(data_ins)
        result = json.loads(dmps(data_ins))
        conn.close()
        return result


if __name__ == '__main__':
    fbs = fb_scraper
    json_data  =  fbs.scrape_data('DataScience.py')
    print(json_data)
    MONGO_HOST=os.getenv('MONGO_HOST')
    MONGO_PORT=os.getenv('MONGO_PORT')
    MONGO_USER=os.getenv('MONGO_USER')
    MONGO_PASS=os.getenv('MONGO_PASS')
    uri = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}'
    fbs.load_data(uri, 'admin', 'fb_page_data',  json_data)