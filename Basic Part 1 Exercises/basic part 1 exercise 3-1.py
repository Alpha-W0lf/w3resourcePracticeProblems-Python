# Write a program to display the current date and time. DONE

from datetime import datetime
import re

now = datetime.now()
now = str(now)
now_short = re.findall('\d+-\d+-\d+\s+\d+:\d+:\d+', now)
# now_short[0] = str(now_short[0])

print(now)
print(now_short)
print('Today\'s date and time are:', now_short[0])
# print(datetime.tzinfo)