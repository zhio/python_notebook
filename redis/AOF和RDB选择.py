"""
可以接受丢失数据 RDB
建议都开启或者定期执行bgsave做快照备份，RDB方式更适合做数据的备份，AOF可以保证数据的不丢失
"""
a = [{'source': 'iep', 'count_time': '2020-07-13', 
'alarm_type': 'Loop', 'type': 'Log', 'count': 236}, 
{'source': 'iep', 'count_time': '2020-07-13', 'alarm_type': 'Loop', 'type': 'Ins', 'count': 48068}, 
{'source': 'iep', 'count_time': '2020-07-13', 'alarm_type': 'Loop', 'type': 'Mer', 'count': 14592}, 
{'source': 'ptd', 'count_time': '2020-07-13', 'alarm_type': 'Alerts', 'type': 'Upd', 'count': 2241}, 
{'source': 'ptd', 'count_time': '2020-07-13', 'alarm_type': 'Alerts', 'type': 'Ins', 'count': 1164}, 
{'source': 'fire', 'count_time': '2020-07-13', 'alarm_type': 'Alerts', 'type': 'Upd', 'count': 2117}, 
{'source': 'fire', 'count_time': '2020-07-13', 'alarm_type': 'Alerts', 'type': 'Ins', 'count': 1}, 
{'source': 'fire', 'count_time': '2020-07-13', 'alarm_type': 'Alerts', 'type': 'Log', 'count': 21189}]


node = {
	"collect": {"iep": 0, "ptd": 0, "hillstone": 0, "star": 0, "gap": 0},
	"event": {"iep": 0, "ptd": 0, "hillstone": 0, "star": 0, "gap": 0},
	"event_update": {"iep": 0, "ptd": 0, "hillstone": 0, "star": 0, "gap": 0},
	"alarm":{"iep": 0, "ptd": 0, "hillstone": 0, "star": 0, "gap": 0},
	"ins": {},
	"mer":{}
}

def fun(i,node_key):
	if i['source'] == 'iep':
		node_key['iep'] = i['count']
	if i['source'] == 'ptd':
		node_key['ptd'] = i['count']
	if i['source'] == 'fire':
		node_key['hillstone'] =i['count']
		node_key['star'] =i['count']
	return node_key


def sum_dict(a,b):
	temp = dict()
	# python3,dict_keys类似set； | 并集
	for key in a.keys()| b.keys():
		temp[key] = sum([d.get(key, 0) for d in (a, b)])
	return temp


for i in a:
	if i['type'] == 'Upd':
		node['event_update'] = fun(i ,node['event_update'])
	if i['type'] == 'Log':
		node['collect'] = fun(i, node['collect'])
	if i['type'] == 'Ins':
		node['ins'] = fun(i, node['ins'])
	if i['type'] == 'Mer':
		node['mer'] = fun(i, node['mer'])
	if i['alarm_type'] == 'Alerts' and  i['type'] == 'Ins':
		node['alarm'] = fun(i, node['alarm'])

	node['event'] = sum_dict(node['ins'], node['mer'])

# print(node)
del node['ins']
del node['mer']
for k, v in node.items():
	print(v)

{'collect': {'iep': 236, 'ptd': 0, 'hillstone': 21189, 'star': 21189, 'gap': 0}, 
'event': {'ptd': 1164, 'star': 1, 'gap': 0, 'iep': 0, 'hillstone': 1}, 
'event_update': {'iep': 0, 'ptd': 2241, 'hillstone': 2117, 'star': 2117, 'gap': 0}, 
'threat_alarm': {'iep': 0, 'ptd': 1164, 'hillstone': 1, 'star': 1, 'gap': 0}, 
'malicious_alarm': {'iep': 0, 'ptd': 0, 'hillstone': 0, 'star': 0, 'gap': 0}}


s = {"a": {"a":1, "b":2},
	"c": {"b":4, "a":3},
	"b": {"a":3, "b":4},}
from collections import OrderedDict
d = sorted(s.items(), key=lambda item: item[0])
print(dict(d))



{'collect': {'iep': 236, 'ptd': 0, 'hillstone': 21189, 'star': 21189, 'gap': 0}, 
'event': {'star': 1, 'gap': 0, 'hillstone': 1, 'ptd': 1164, 'iep': 0}, 
'event_update': {'iep': 0, 'ptd': 2241, 'hillstone': 2117, 'star': 2117, 'gap': 0}, 
'threat_alarm': {'iep': 0, 'ptd': 1164, 'hillstone': 1, 'star': 1, 'gap': 0}, 
'malicious_alarm': {'iep': 0, 'ptd': 0, 'hillstone': 0, 'star': 0, 'gap': 0}}
