from fastapi import FastAPI
from scraper import *
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

def home_root():
    '''home root'''
    return {"Hello": "World"}


@app.get("/page/{name}")
def scrape_load_db(name: str):
    '''root to scrape fb page and load to db'''
    fbs = fb_scraper
    json_data  =  fbs.scrape_data(name)
    MONGO_HOST=os.getenv('MONGO_HOST')
    MONGO_PORT=os.getenv('MONGO_PORT')
    MONGO_USER=os.getenv('MONGO_USER')
    MONGO_PASS=os.getenv('MONGO_PASS')
    uri = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}'
    result = fbs.load_data(uri, 'admin', 'fb_page_data',  json_data)
    return result
