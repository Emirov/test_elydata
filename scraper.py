from facebook_page_scraper import Facebook_scraper
from pymongo import MongoClient
import json

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
        conn.close()
        return json_data


if __name__ == '__main__':
    fbs = fb_scraper
    json_data  =  fbs.scrape_data('metaai')
    uri = 'mongodb://admin:Admin1337@localhost:27017'
    fbs.load_data(uri, 'admin', 'fb_page_data',  json_data)
