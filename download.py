#coding:utf-8
import urllib2
def download(url,num_retries=2):
	print("Downloading:%s\n"%url)
	try:
		html=urllib2.urlopen(url).read()
	except urllib2.URLError,e:
		print("download error:%s"%e.reason)
		html=None
		if hasattr(e,'code') and 500 <= e.code <= 600:
			return download(url,num_retries-1)
	return html
	
print(download("http://httpstat.us/500"))

		
	