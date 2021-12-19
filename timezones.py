from datetime import datetime
import pytz

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print(bogota_date.strftime('En bogotá son las %H:%M'))