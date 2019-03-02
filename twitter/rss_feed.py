import feedparser
from urlextract import URLExtract

def Divition(list):
    list = list.split('\t')
    list = ''.join(list)
    list = list.split('<br>')
    list = ''.join(list)
    list = list.split('</a>')
    list = ''.join(list)
    list = list.split('\n')
    return list

feed = feedparser.parse('https://yify.is/api/rss')
feed = feed['entries'][0]['summary_detail']['value']
feed = Divition(feed)
extractor = URLExtract()
image_link = extractor.find_urls(feed[1])
description = feed[6]












#  link = feed['entries'][0]['link']
#  title = feed['entries'][0]['title']
#  resumet = feed['entries'][0]['summary_detail']['value']


