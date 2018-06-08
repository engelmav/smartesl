import os
import json
from logger import log

config_path = os.getenv('SMARTEFL_CONFIG')

if config_path is None:
    raise RuntimeError('You must specify your config file path'
                       'by setting SMARTEFL_CONFIG.')

environment = 'test'
log.debug("Using config from %s", config_path)

with open(config_path) as f:
    config_str = f.read()
    config_json = json.loads(config_str)
    db_conn_str = config_json[environment]['db_connection_str']



