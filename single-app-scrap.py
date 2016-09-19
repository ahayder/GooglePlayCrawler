import urllib
import re
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET

app_url = "https://play.google.com/store/apps/details?id=[HERE PUT THE APP ID]"
link = urllib.urlopen(app_url)
html = link.read()

regex_for_icon = '<img class="cover-image" src="(.+?)" alt="Cover art" aria-hidden="true" itemprop="image">'
regex_for_app_name = '<div class="document-title" itemprop="name"> <div>(.+?)</div> </div>'
regex_for_dev_name = '<span itemprop="name">(.+?)</span>'
regex_for_reviews = '<span class="reviews-num">(.+?)</span>'
regex_for_ratings = '<div class="score">(.+?)</div>'
regex_for_update = '<div class="content" itemprop="datePublished">(.+?)</div>'

icon_re = re.compile(regex_for_icon)
app_name_re = re.compile(regex_for_app_name)
dev_name_re = re.compile(regex_for_dev_name)
reviews_re = re.compile(regex_for_reviews)
ratings_re = re.compile(regex_for_ratings)
update_re = re.compile(regex_for_update)

icon_link = re.findall(icon_re, html)
app_name = re.findall(app_name_re, html)
dev_name = re.findall(dev_name_re, html)
reviews = re.findall(reviews_re, html)
ratings = re.findall(ratings_re, html)
updated = re.findall(update_re, html)


app_market = ET.Element("app_market")

app = ET.SubElement(app_market, "app")

name_xml = ET.SubElement(app, "name")
name_xml.text = app_name[0]

developer_xml = ET.SubElement(app, "developer")
developer_xml.text = dev_name[0]

last_upadate_xml = ET.SubElement(app, "last_update")
last_upadate_xml.text = updated[0]

review_xml = ET.SubElement(app, "reviews")
review_xml.text = reviews[0]

ratings_xml = ET.SubElement(app, "ratings")
ratings_xml.text = ratings[0]

url_xml = ET.SubElement(app, "url")
url_xml.text = app_url

icon_ulr_xml = ET.SubElement(app, "icon_url")
icon_ulr_xml.text = icon_link[0]


app_market = ET.ElementTree(app)
app_market.write("app.xml")
