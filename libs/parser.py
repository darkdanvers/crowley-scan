#
#  parser.py
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
