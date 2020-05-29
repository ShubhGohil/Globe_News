from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from news.models import Headline
import requests
# Create your views here.

# GEtting news from Times of India
requests.packages.urllib3.disable_warnings()
def scrape(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bo.html)"}
	url = "https://timesofindia.indiatimes.com/briefs"
	
	content = session.get(url, verify=False).content
	soup = BeautifulSoup(content, 'html.parser')
	News = soup.find_all('div', {"class":"brief_box"})
	for article in News:
		try:
			main = article.find('h2').find('a')
		except Exception as e:
			print(e)
		link = str(main['href'])
		link = url+link
		title = main.text
		#image_src = article.find('a')
		#image_src = article.find('div', {"class":"posrel"})
		#image = image_src.find('img')['src']
		#print(image_src)
		new_headline = Headline()
		new_headline.title = title
		#new_headline.image = image
		new_headline.url = link	
		new_headline.save()
	
	return redirect('../')
	
	
def news_list(request):
	headlines = Headline.objects.all()[::-1]	
	context = {
		'object_list':headlines,
	}
	return render(request, "index.html", context)
	
