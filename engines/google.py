import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from libs.parser import Parser
from libs.randomize import Randomize
from libs.logging import log_info

class SearchGoogle():
    def __init__(self, query, number_of_results,
                timeout):

        self.query = query
        self.start_page = 0
        self.number_of_results = number_of_results
        self.timeout_requests = timeout        
        self.failed_request = 'Our systems have detected unsual traffic from\
                                your computer network'
        
        self.filter_string = ["google"]
        self.randomize = Randomize()
        self.parser = Parser()
    
    def search_results(self):
        parameters = {'q': self.query, 'start': self.start_page,
                      'num': self.number_of_results}
        
        user_agent = self.randomize.get_random_user_agent()
        google_url = self.randomize.get_random_google_url()

        log_info("Searching")
        log_info(user_agent)
        log_info("Google URL {0}".format(google_url))

        response = requests.get(url=google_url,
                                params=parameters, 
                                timeout=self.timeout_requests,
                                headers=user_agent)
        
        if self.failed_request in response:
            logo_danger("Google detected malicious traffic")
            return 1

        bs = BeautifulSoup(response.text, "lxml")
        
        links = bs.find_all("a")
        links = self.parser.remove_bad_urls(self.filter_string, links)

        log_info("Number of targets: {0}".format(len(links)))
        print("-" * 79)

        return links
