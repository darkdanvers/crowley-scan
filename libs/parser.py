from urllib.parse import urlparse
from libs.logging import log_danger 

class Parser():

    def url_parser(self, url):
        parser_url = urlparse(url)
        return bool(parser_url.scheme)

    def remove_bad_urls(self, filter_string, results):
        results_parsed = []

        for link in results:
            if 'href' in link.attrs:
                url = link.attrs["href"]

                if(self.url_parser(url)):
                    for string in filter_string:
                        if string not in url:
                            results_parsed.append(url)

        return results_parsed

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
            log_danger("SQL Injector failed to inject SQL into target {0}".format(target))
        
        return domains


