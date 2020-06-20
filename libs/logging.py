def banner():
    banner = '''
 _____                   _            
/  __ \                 | |           
| /  \/_ __ _____      _| | ___ _   _ 
| |   | '__/ _ \ \ /\ / / |/ _ \ | | |
| \__/\ | | (_) \ V  V /| |  __/ |_| |
 \____/_|  \___/ \_/\_/ |_|\___|\__, |
                                 __/ |
                                |___/ 

Author: bsd0x
Email: root@bsd0x.me
Version: v1.0.0
    '''

    print(banner)

def log_info(msg):
    print("\033[1;92m[INFO] {0}\033[0;0m".format(msg))

def log_danger(msg):
    print("\033[1;91m[DANGER] {0}\033[0;0m".format(msg))

def log_warning(msg):
    print("\033[1;93m[WARNING] {0}\033[0;0m".format(msg))

def log_vulnerable(msg):
    print("\033[1;93m[VULL] {0}\033[0;0m".format(msg))

