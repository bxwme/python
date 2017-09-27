#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 手機號歸屬地查詢
# 結果爲   手機號,歸屬地,運營商
import urllib2
import urllib
from lxml import etree
def findPlace(phone):
	data = {}
	data['haomas'] = phone
	data['Submit'] = '(unable to decode value)'
	url = 'http://www.1234i.com/fj.php'
	post_data = urllib.urlencode(data)
	#提交，发送数据
	req = urllib2.urlopen(url, post_data)
	#获取提交后返回的信息
	content = req.read()
	tree = etree.HTML(content)
	return tree.xpath('//ol/li/text()')



if __name__ == "__main__":
	print findPhone('18040876521')  #多個手機號用空格分割
	
