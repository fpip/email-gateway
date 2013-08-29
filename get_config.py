import os
from ConfigParser import SafeConfigParser as ConfigParser

config_in_home = os.path.join(os.environ.get('HOME', ''), '.email_gateway')
config_in_etc = "/etc/email_gateway.cfg"
config_filename = config_in_home \
        if os.path.exists(config_in_home) \
        else config_in_etc

config = ConfigParser()
with open(config_filename) as fp:
    config.readfp(fp)
