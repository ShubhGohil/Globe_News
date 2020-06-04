from django.urls import path
from news.views import scrape, news_list, market_news_list, scrape_market, cricket_news_list, scrape_cric
urlpatterns = [
	path('scrape/', scrape, name = "scrape"),
	path('', news_list, name="index"),
	path('market.html/marketscrape/', scrape_market, name = "marketscrape"),
	path('market.html/', market_news_list, name="market"),
	path('cricket.html/cricscrape/', scrape_cric, name = "cricscrape"),
	path('cricket.html/', cricket_news_list, name="cricket"),


]
