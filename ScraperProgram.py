# Import classes (To be updated...?)
from Scraper import Scraper
from TwitterScraper import TwitterScraper
from RedditScraper import RedditScraper

def main():
    #Tentatively we can use the console as a UI to let the user key in the search term 
    #and to choose to crawl twitter or reddit?

    twitter_crawler = TwitterScraper("moderna vaccine", 20)
    twitter_crawler.scrape()

if __name__ == '__main__':
    main()

