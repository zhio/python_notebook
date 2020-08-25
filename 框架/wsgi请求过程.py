"""
浏览器发送的请求被Nginx监听到，Nginx会根据请求的url path把请求的静态资源分发给静态资源目录，
别的请求根据配置好的转发到相应端口。
实现了wsgi的程序会监听某个端口，监听到Nginx转发过来的请求接收后(一般用socket的recv来接收HTTP的报文)
以后把请求的报文封装成environ的字典对象，然后再提供一个start_response的方法。
把这两个对象当成参数传入某个方法比如wsgi_app(environ, start_response)或者
实现了__call__(self, environ, start_response)方法的某个实例。
这个实例再调用start_response返回给实现了WSGI的中间件，再由中间件返回给Nginx。
"""