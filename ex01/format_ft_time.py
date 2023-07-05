import time
import datetime

time_seconds = time.time()
time_seconds_scientific = time_seconds
time_datetime = datetime.datetime.fromtimestamp(time_seconds)
time_string = time_datetime.strftime('%B %d %Y')
print('{}: {:,.4f} or {:.2e} {}'
      .format('Seconds since January 1, 1970',
              time_seconds,
              time_seconds_scientific,
              'in scientific notation'))
print(time_string)
