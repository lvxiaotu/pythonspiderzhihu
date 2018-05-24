# pythonspiderzhihu
爬取知乎的图片

知乎问题的数据是通过ajax请求数据，加载传过来json

所以只要拿到json就拿到了数据

url中必须要带include这个查询字符串参数，否则返回的json不全

url中 limit是回答的个数 offest是偏移量

headers 中 一定要带cookie 否则会报没有认证通过

