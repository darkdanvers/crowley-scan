#
#  sql_injection.py
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

from libs.randomize import Randomize
from libs.parser import Parser
from libs.logging import *
from urllib.parse import urlparse
from vull.reporting import ReportVulnerabilities

class SqlInjection(ReportVulnerabilities):
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
            "Microsoft Access Driver",
            "General SQL Server error: Check messages from the SQL Server",
            "mssql_query"
        ]

    def insert_sqli_payloads(self, url):
        domains = []
        parser_url = urlparse(url)

        domain = url.split('?')[0]        
        querys = parser_url.query.split("&")

        payloads = ("'")

        try:
            for payload in payloads:
                domain_with_payload = domain + "?" + ("&".join([query + payload 
                                                      for query in querys]))

                domains.append(domain_with_payload)
        except:
            log_error("SQL Injector failed to inject SQL into target {0}".format(target))
        
        return domains

    def check_have_sqli(self, target_response):
        for error in self.error_list:
            if error in target_response.text:
                return True
        
        return False
        
    def check_vull(self, target):
        targets_with_payloads = self.insert_sqli_payloads(target)

        for target in targets_with_payloads:
            user_agent = self.randomize.get_random_user_agent()

            try:
                response = requests.get(url=target, headers=user_agent)
                http_status_code = response.status_code

                log_info(target)

                have_sqli = self.check_have_sqli(response)

                if have_sqli:
                    log_vulnerable(target)

                    target_report = {'target': target,
                                      'user_agent': user_agent,
                                      'http_status_code': http_status_code,
                                      'engine': 'google',
                                      'vulnerabilities': 'SQL Injection'}

                    self.describe_target.append(target_report.copy())
            except:
                log_error("{0} have error in request".format(target))
