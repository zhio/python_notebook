"""
请求一些缓存中不存在的key，请求打到后端
解决：
请求参数验证，无效请求直接返回
对缓存中找不到的key，需要去数据库查找的key，缓存到Redis中，但是可能会导致Redis中缓存大量无效的key，可以设置一个很短的过期时间，例如1分钟
布隆过滤器，将所有可能的存在的数据通过去hash值的方式存入到一个足够大的bitmap中去，处理请求时，通过在botmap中查找，可以将不存在的数据拦截掉。
"""