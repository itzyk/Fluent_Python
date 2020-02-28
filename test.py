# import urllib2
# import random
#
# proxy_list = [
#     {"https": "222.173.10.82:8888"},
# ]
#
# proxy = random.choice(proxy_list)
# httpproxy_handler = urllib2.ProxyHandler(proxy)
#
# opener = urllib2.build_opener(httpproxy_handler)
#
# request = urllib2.Request("http://www.baidu.com/")
# response = opener.open(request)
# print response.read()

import requests

proxies = {
  # "http": "http://12.34.56.79:9527",
  "https": "https://222.173.10.82:8888",
}
response = None
try:
    # response = requests.get("https://vipreader.qidian.com/chapter/1015279653/519649219", proxies=proxies)
    raise requests.exceptions.ProxyError

except requests.exceptions.ConnectionError:
    print "catched success!!! "

except Exception,e:
    print "excep"



