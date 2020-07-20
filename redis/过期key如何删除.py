"""
redis处理过期key有三种策略
1、惰性删除
	访问key的时候，如果发现key已经过期，那么会被删除
2、定期删除
	redis配置项hz定义了serverCron时间事件任务执行周期，每秒运行10次，扫描db中100key，如果过期就删除
	如果超过25key过期，继续清理
3、超出maxmemory触发淘汰策略
	noeviction：不删除key，返回内存溢出错误
	allkeys-random：从所有的key中随机挑选key，进行淘汰
	allkeys-lru：从所有key中最近使用时间距离现在最远的key，进行淘汰
	allkeys-lfu：就是从所有的key中挑选使用频率最低的key，进行淘汰
	volatile-random：从设置了过期时间的结果集中随机挑选key删除
	volatile-lru：从设置了过期时间的结果集中上次使用时间距离现在最久的key开始删除
	volatile-lfu：从设置了过期时间的结果集中可存活时间最短的key开始删除(也就是从哪些快要过期的key中先删除)
	volatile-ttl：从过期时间的结果集中选择使用频率最低的key开始删除

"""