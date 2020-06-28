#
#  logging.py
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

def log_info(msg):
    print("\033[1;92m[INFO] {0}\033[0;0m".format(msg))

def log_error(msg):
    print("\033[1;91m[ERROR] {0}\033[0;0m".format(msg))

def log_vulnerable(msg):
    print("\033[1;93m[VULL] {0}\033[0;0m".format(msg))

def log_report_targets_vulnerables(target, engine, http_status_code, vulnerabilities):
    print("-" * 79)
    
    output = '''\033[1;93m
Target: {0}
Engine: {1}
HTTP Status code: {2}
Vulnerabilitie: {3}\033[0;0m'''.format(target, engine, http_status_code, vulnerabilities)

    print(output)
