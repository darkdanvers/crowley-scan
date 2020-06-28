#
#  randomize.py
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

import random

class Randomize():

    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
            "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
            "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
            "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
            "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
            "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0",
            "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0"
        ]

        self.google_urls_list = [
            'www.google.com', 'www.google.ac', 'www.google.com.om',
            'www.google.ad', 'www.google.ae', 'www.google.com.af',
            'www.google.com.ag', 'www.google.com.ai', 'www.google.am',
            'www.google.it.ao', 'www.google.com.ar', 'www.google.cat',
            'www.google.as', 'www.google.at', 'www.google.com.au',
            'www.google.az', 'www.google.ba', 'www.google.com.bd',
            'www.google.be', 'www.google.bf', 'www.google.bg',
            'www.google.com.bh', 'www.google.bi', 'www.google.bj',
            'www.google.com.bn', 'www.google.com.bo', 'www.google.com.br',
            'www.google.bs', 'www.google.co.bw', 'www.google.com.by',
            'www.google.com.bz', 'www.google.ca', 'www.google.com.kh',
            'www.google.cc', 'www.google.cd', 'www.google.cf',
            'www.google.cn', 'www.google.com.co', 'www.google.co.nz',
            'www.google.cg', 'www.google.ch', 'www.google.ci',
            'www.google.co.ck', 'www.google.cl', 'www.google.cm',
            'www.google.co.cr', 'www.google.com.cu', 'www.google.cv',
            'www.google.cz', 'www.google.de', 'www.google.nu',
            'www.google.dj', 'www.google.dk', 'www.google.dm',
            'www.google.com.do', 'www.google.dz', 'www.google.no',
            'www.google.com.ec', 'www.google.ee', 'www.google.com.eg',
            'www.google.es', 'www.google.com.et', 'www.google.com.np',
            'www.google.fi', 'www.google.com.fj', 'www.google.fm',
            'www.google.fr', 'www.google.ga', 'www.google.nl',
            'www.google.ge', 'www.google.gf', 'www.google.gg',
            'www.google.com.gh', 'www.google.com.gi', 'www.google.nr',
            'www.google.gl', 'www.google.gm', 'www.google.gp',
            'www.google.gr', 'www.google.com.gt', 'www.google.com.ni',
            'www.google.gy', 'www.google.com.hk', 'www.google.hn',
            'www.google.hr', 'www.google.ht', 'www.google.com.ng',
            'www.google.hu', 'www.google.co.id', 'www.google.iq',
            'www.google.ie', 'www.google.co.il', 'www.google.com.nf',
            'www.google.im', 'www.google.co.in', 'www.google.io',
            'www.google.is', 'www.google.it', 'www.google.ne',
            'www.google.je', 'www.google.com.jm', 'www.google.jo',
            'www.google.co.jp', 'www.google.co.ke', 'www.google.com.na',
            'www.google.ki', 'www.google.kg', 'www.google.co.kr',
            'www.google.com.kw', 'www.google.kz', 'www.google.co.mz',
            'www.google.la', 'www.google.com.lb', 'www.google.com.lc',
            'www.google.li', 'www.google.lk', 'www.google.com.my',
            'www.google.co.ls', 'www.google.lt', 'www.google.lu',
            'www.google.lv', 'www.google.com.ly', 'www.google.com.mx',
            'www.google.co.ma', 'www.google.md', 'www.google.me',
            'www.google.mg', 'www.google.mk', 'www.google.mw',
            'www.google.ml', 'www.google.mn', 'www.google.ms',
            'www.google.com.mt', 'www.google.mu', 'www.google.mv',
            'www.google.com.pa', 'www.google.com.pe', 'www.google.com.ph',
            'www.google.com.pk', 'www.google.pn', 'www.google.com.pr',
            'www.google.ps', 'www.google.pt', 'www.google.com.py',
            'www.google.com.qa', 'www.google.ro', 'www.google.rs',
            'www.google.ru', 'www.google.rw', 'www.google.com.sa',
            'www.google.com.sb', 'www.google.sc', 'www.google.se',
            'www.google.com.sg', 'www.google.sh', 'www.google.si',
            'www.google.sk', 'www.google.com.sl', 'www.google.sn',
            'www.google.sm', 'www.google.so', 'www.google.st',
            'www.google.com.sv', 'www.google.td', 'www.google.tg',
            'www.google.co.th', 'www.google.tk', 'www.google.tl',
            'www.google.tm', 'www.google.to', 'www.google.com.tn',
            'www.google.com.tr', 'www.google.tt', 'www.google.com.tw',
            'www.google.co.tz', 'www.google.com.ua', 'www.google.co.ug',
            'www.google.co.uk', 'www.google.us', 'www.google.com.uy',
            'www.google.co.uz', 'www.google.com.vc', 'www.google.co.ve',
            'www.google.vg', 'www.google.co.vi', 'www.google.com.vn',
            'www.google.vu', 'www.google.ws', 'www.google.co.za',
            'www.google.co.zm', 'www.google.co.zw'
        ]

    def get_random_user_agent(self):
        user_agent = random.choice(self.user_agent_list)
        return {'User-Agent': user_agent}
    
    def get_random_google_url(self):
        random_url = random.choice(self.google_urls_list)
        url_formated = "http://{0}/search".format(random_url)
        return url_formated
