import calendar
from datetime import datetime, timedelta

import tzlocal
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                millis = int(
                    calendar.timegm(obj.timetuple()) * 1000 +
                    obj.microsecond / 1000
                )
                date = '-'.join((str(obj.year), str(obj.month).rjust(2, '0'), str(obj.day).rjust(2, '0')))
                time = ':'.join((str(obj.hour).rjust(2, '0'), str(obj.minute).rjust(2, '0'), str(obj.second).rjust(2, '0')))

                # TODO probably not the best solution
                cet = tzlocal.get_localzone()
                offset = cet.utcoffset(datetime.utcnow())
                offset_string = str(int(offset.seconds / 3600)).rjust(2, '0').ljust(4, '0')

                return date + 'T' + time + '+' + offset_string
            elif isinstance(obj, timedelta):
                return obj.total_seconds()
            iterable = iter(obj)
        except TypeError as e:
            print (e)
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
