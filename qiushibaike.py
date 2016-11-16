# -*-coding=utf-8 -*-
"""
	date: 2016.7.9
	网站改版 已失效 需修改后使用
	爬取糗事百科的笑话 写入D:/1.txt文件
"""

import urllib
import urllib2
import re

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36'
headers = { 'User-Agent' : user_agent }

pre = 'http://www.qiushibaike.com/textnew/page/'
pattern = re.compile(r"""</h2>.*?content">

(.*?)
<!--""", re.S)
# pattern = re.compile(r"""content">

# 		(.*?)
# 		<!--.*?"stats-vote">""", re.S)

def getJoke(i):
	url = pre + str(i)
	try:
	    request = urllib2.Request(url, headers=headers)
	    response = urllib2.urlopen(request)
	    content = response.read()
	except urllib2.URLError, e:
	    if hasattr(e, 'code'):
	        print e.code
	    if hasattr(e, 'reason'):
	        print e.reason

	items = re.findall(pattern, content)
	items = (n.replace(r'<br/>',' ') for n in items)
	for item in items:
	    f.write(item)
	    f.write('\n')

f = open('D:/1.txt','w')
# f.write('123')
for i in range(1,36):
	getJoke(i)
	print i
f.close()
