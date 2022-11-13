import datetime


def get_timestamp():
    utc_date_time = datetime.datetime.now(tz=datetime.timezone.utc)
    str_utc_date_time = utc_date_time.isoformat('T')
    str_utc_date_time = str_utc_date_time[0:-9]
    str_utc_date_time += 'Z'
    return str_utc_date_time


print(get_timestamp())
