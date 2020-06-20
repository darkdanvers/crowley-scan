import requests

from libs.randomize import Randomize
from libs.parser import Parser
from libs.logging import *

class SqlInjection():
    def __init__(self):
        self.parser = Parser()
        self.randomize = Randomize()
        self.report_targets_vull = []
        self.error_list = [
            "mysql_fetch_array()", 
            "You have an error in your SQL syntax",
            "MySQL Query fail.",
            "PostgreSQL ERROR",
            "Access Database Engine",
            "Microsoft Access Driver"
        ]

    def report(self):
        print("*" * 79)
        log_info("Number of vulnerable sites: {0}".format(len(self.report_targets_vull)))
        
        for target in self.report_targets_vull:
            log_info(target)

    def check_vull(self, target):
        targets_with_payloads = self.parser.insert_sqli_payloads(target)

        for target in targets_with_payloads:
            user_agent = self.randomize.get_random_user_agent()
            log_info(target)

            try:
                response = requests.get(url=target, headers=user_agent)

                for error in self.error_list:
                    if error in response.text:
                        log_vulnerable("{0} is vulnerable".format(target))
                        self.report_targets_vull.append(target)
            except:
                log_danger("{0} have error in request".format(target))
