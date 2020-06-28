#
#  google.py
#  
#  Copyright 2020 Gabriel "bsd0x" Dutra <root@bsd0x.me>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

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
