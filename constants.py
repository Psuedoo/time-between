from pytz import timezone
from datetime import datetime

tz = timezone("US/Eastern")
my_date = datetime(2021, 5, 29, tzinfo=tz)
