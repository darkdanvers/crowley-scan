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
