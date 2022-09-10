from .models import Article
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


def daily_hodl_scraper(pages):
        main_url = "https://dailyhodl.com/?s=nft"

        for page in range(1,pages+1):
            if page == 1:
                url = main_url
            else:
                url = "https://dailyhodl.com/page/" + str(page) + "/?s=nft"
        
            response = requests.get(url)
            soup = bs(response.content, 'html.parser' )
            news = soup.find_all("div" , {"class" : "jeg_postblock_content"})
            latest = Article.objects.filter(source__iexact = 'dailyhodl').latest('date')    # need to make this a try statement, in case database is empty 
            

            for article in news:
                if latest.title != article.h3.a.text.strip():   # stops saving items when it gets to latest saved article
                    story = Article()

                    # save each article
                    story.title = article.h3.a.text.strip()
                    story.link = article.a['href']
                    story.date = datetime.strptime(article.find("div", {"class" : "jeg_meta_date"}).text.strip(), '%B %d, %Y')
                    story.author = article.find("div", {"class" : "jeg_meta_author"}).a.text.strip()
                    story.description = article.find("div", {"class" : "jeg_post_excerpt"}).p.text.strip()
                    story.source = "dailyhodl"
                    story.save()
                else:
                    break       


                
                
