from datetime import datetime
from dateutil import relativedelta
from pytz import timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def root():
    return {'response': 'OK'}

@app.get("/diff/")
async def get_diff():
    tz = timezone('US/Eastern')

    date_one = datetime(2021, 5, 29, tzinfo=tz)
    date_two = datetime.now(tz=tz)


    diff = relativedelta.relativedelta(date_two, date_one)

    return {'years': diff.years, 'months': diff.months, 'days': diff.days}