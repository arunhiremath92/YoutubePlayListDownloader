import requests
from lxml import html
from HTMLParser import HTMLParser
from subprocess import call,check_call
page = requests.get('https://www.youtube.com/playlist?list=PL2_aWCzGMAwLSqGsERZGXGkA5AfMhcknE')
tree = html.fromstring(page.text)
playlist = tree.xpath('//*[@id="pl-load-more-destination"]/tr/td[4]/a')

for video in playlist:
	title=video.text
	data=video.get('href')
	#data=data[7:len(data)]
	print title
	videoId=data.split("&")[0]
	print "Starting the download"	
	call(["you-get", "https://www.youtube.com"+videoId])
	while check_call(["you-get", "https://www.youtube.com"+videoId]):
		print "waiting for it to complete"
	
		
