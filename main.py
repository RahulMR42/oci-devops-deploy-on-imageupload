from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version = os.getenv('image_url', default = '0.0.9')
    return {"Message": "Its me Rahul","Version":version}

