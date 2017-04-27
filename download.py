#coding:utf-8
import urllib2
import re
def download(url,user_agent="wswp",num_retries=2):
	print("Downloading:%s\n"%url)
	headers={'user_agent':user_agent}
	request=urllib2.Request(url,headers=headers)
	try:
		html=urllib2.urlopen(request).read()
	except urllib2.URLError,e:
		print("download error:%s"%e.reason)
		html=None
		if num_retries>0:
			if hasattr(e,'code') and 500 <= e.code <= 600:
				return download(url,num_retries-1)
		else:
			return None
	return html
	
def get_links(html):
	webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return webpage_regex.findall(html)
	
	
def link_crawl(seed_url,link_regex):
	crawl_queue = [seed_url]
	seen = set(crawl_queue)
	while crawl_queue:
		url = crawl_queue.pop()
		html=download(url)
		for link in get_links(html):
			if re.match(link_regex,link):
				link = urlparse.urljoin(seed_url,link)
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)
	

print(link_crawl("http://example.webscriping.com",'/(index|view)'))		
	