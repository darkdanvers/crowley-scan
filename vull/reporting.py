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
