from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from news.models import Headline,MarketHeadline,CricHeadline
import requests
# Create your views here.

# Getting news from Times of India
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
	
	
	
def scrape_market(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bo.html)"}
	url = "https://www.economist.com/finance-and-economics/"
	linker = "https://www.economist.com"
	content = session.get(url, verify=False).content
	soup = BeautifulSoup(content, 'html.parser')
	News = soup.find_all('div', {"class":"teaser__text"})
	for article in News:	
		try:
			main = article.find('h2').find('a')
		except Exception as e:
			print(e)
		link = str(main['href'])
		link = linker+link
		title = main.find_all('span')[-1]
		title = title.text
		#image_src = article.find('a')
		#image_src = article.find('div', {"class":"posrel"})
		#image = image_src.find('img')['src']
		#print(image_src)
		new_headline = MarketHeadline()
		new_headline.title = title
		#new_headline.image = image
		new_headline.url = link	
		new_headline.save()
	
	return redirect('../')

	
def scrape_cric(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bo.html)"}
	url = "https://www.cricbuzz.com/cricket-news"
	linker = "https://www.cricbuzz.com"
	content = session.get(url, verify=False).content
	soup = BeautifulSoup(content, 'html.parser')
	News = soup.find_all('h2', {"class":"cb-nws-hdln cb-font-18 line-ht24"})
	print(News[0])
	for article in News:
		try:
			main = article.find('a')
			print(main)
		except Exception as e:
			print(e)
		link = str(main['href'])
		link = linker+link
		print(link)
		title = main.text
		print(title)
		#image_src = article.find('a')
		#image_src = article.find('div', {"class":"posrel"})
		#image = image_src.find('img')['src']
		#print(image_src)
		new_headline = CricHeadline()
		new_headline.title = title
		#new_headline.image = image
		new_headline.url = link	
		new_headline.save()
	
	return redirect('../')
	
	
	
	
def news_list(request):
	headlines = Headline.objects.all()[120::-1]	
	context = {
		'object_list':headlines,
	}
	return render(request, "index.html", context)


def market_news_list(request):
	headlines = MarketHeadline.objects.all()[::-1]	
	context = {
		'object_list':headlines,
	}
	return render(request, "market.html", context)
	
def cricket_news_list(request):
	headlines = CricHeadline.objects.all()[::-1]	
	context = {
		'object_list':headlines,
	}
	return render(request, "cricket.html", context)
