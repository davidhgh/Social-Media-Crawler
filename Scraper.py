from abc import ABCMeta,abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Scraper(metaclass=ABCMeta):
    url = ''
    query = ''
    fully_qualified_domain = ''
    sample_size = 0
    counter = 0     #not used, remove???
    last_position = None
    end_of_scroll_region = False

    def __init__(self, query, sample_size):
        self.query = query
        self.sample_size = sample_size

    @property
    def query(self):
        return self.__query
    @query.setter
    def query(self, query):
        self.__query = query

    @property
    def sample_size(self):
        return self.__sample_size
    @sample_size.setter
    def sample_size(self, sample_size):
        self.__sample_size = sample_size

    def scroll_down_page(self, driver, last_position, num_seconds_to_load=0.5, scroll_attempt=0, max_attempts=5):
        end_of_scroll_region = False
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(num_seconds_to_load)
        curr_position = driver.execute_script("return window.pageYOffset;")
        if curr_position == last_position:
            if scroll_attempt < max_attempts:
                end_of_scroll_region = True
            else:
                self.scroll_down_page(last_position, curr_position, scroll_attempt + 1)
        last_position = curr_position
        return last_position, end_of_scroll_region

    #Starts instance of web
    def initialise_webdriver(self, fqdn):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(fqdn)
        sleep(3)
        return browser

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def scrape(self):
        pass
    
    @abstractmethod
    def csv_writer(self):
        pass
