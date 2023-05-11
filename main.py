import string
from xmlrpc.client import boolean
from fastapi import FastAPI

from get_screenshot import create_screenshot


app = FastAPI()


@app.get("/")
def get_screenshot(url, fullscreen: boolean):
    try:
        create_screenshot(url, fullscreen)
        return {"Response": "200"}
    except:
        return {"Error": "400"}
