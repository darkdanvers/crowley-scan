from urllib.parse import urlparse

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
