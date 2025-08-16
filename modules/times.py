from datetime import datetime

import pytz
from dateutil import tz


def time_now(nice_format: bool = False) -> datetime | str:
    if nice_format:
        return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return datetime.now()


def str_to_time(str_time):
    return pytz.utc.localize(
        datetime.strptime(str_time, '%Y-%m-%d'))


def compare_time(older, 
                 newer):
    return older < newer
        

def locate_date(str_time, template='%Y-%m-%dT%H:%M:%S.%f%z'):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    return datetime.strptime(str_time, template
                             ).replace(tzinfo=from_zone).astimezone(to_zone)