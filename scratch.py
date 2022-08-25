import datetime
from datetime import timedelta

today = datetime.date.today()
days_45 = timedelta(days = 90)
result = today - days_45
print(today)
print(result)
