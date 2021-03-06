"""
CORS是一个W3C标准,全称是“跨域资源共享"(Cross-origin resoure sharing). 
它允许浏览器向跨源服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制。

CSRF防御方式
	后端生成表单时会生成一串随机token，内置到表单里成为一个字段，同时把此串token存入session中,
	每次表单提交到后端时都会检查这两个值是否一致，以此来判断此次表单提交是否是可信的，
	提交过一次之后，如果这个页面没有生成CSRF token,那么token将会被清空,如果有新的需求，
	那么token会被更新。 攻击者可以伪造POST表单提交，但是他没有后端生成的内置于表单的token，
	session中没有token都无济于事。
"""