#
#  reporting.py
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

from libs.logging import log_report_targets_vulnerables

class ReportVulnerabilities():
    describe_target = []

    def create_report(self):
        for target_desc in self.describe_target:
            target = target_desc["target"]
            http_status_code = target_desc["http_status_code"]
            engine = target_desc["engine"]
            vulnerabilitie = target_desc["vulnerabilities"]
            
            log_report_targets_vulnerables(target, engine, http_status_code, vulnerabilitie)
