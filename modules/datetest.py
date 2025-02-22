import datetime
from datetime import timedelta

date0 = datetime.datetime(2022,12,25,11,34)
print(date0)
date0 = date0 + timedelta(hours = 20)

print(date0)

