from datetime import datetime
from dateutil import relativedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from constants import tz, my_date

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"response": "OK"}


@app.get("/diff/")
async def get_diff():

    date_two = datetime.now(tz=tz)

    diff = relativedelta.relativedelta(date_two, my_date)

    return {"years": diff.years, "months": diff.months, "days": diff.days}
