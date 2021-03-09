from Scraper import Scraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
import constants as const

class RedditScraper(Scraper):
    def __init__(self, query, sample_size, subreddit):
        super().__init__(query, sample_size)
        self.__subreddit = subreddit

    @property
    def subreddit(self):
        return self.__subreddit
    @subreddit.setter
    def subreddit(self,subreddit):
        self.__subreddit = subreddit

    # def scrape(self):
    #     return
        