from fastapi import FastAPI
import scraper
app = FastAPI()


@app.get("/")
def home_root():
    '''home root'''
    return {"Hello": "World"}