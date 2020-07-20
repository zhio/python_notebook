types_dict = {
            "1": ['h_event_load', 'hahah'],
            "2": 'h_threat_alarm_event',
            "3": "h_threat_alarm_event",
            "4": "h_threat_alarm_event",
            "5": "h_threat_alarm_event"
        }
print(types_dict.get('1')[0])
print(types_dict.get('1')[1])


print(tuple([]))

print("'{}' 123".format('hehko'))

import time
s =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(s)

d = {}
if d:
	print('2222')

from tkinter import _flatten
lst = [1, 2, [3, [4], [5, 6], 7], 8] * 1000000
print(_flatten(lst))