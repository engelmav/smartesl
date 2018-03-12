import os
import json
from logger import log

config_path = os.getenv('SMARTEFL_CONFIG')

if config_path is None:
    raise RuntimeError('You must specify your db config file'
                       'by setting SMARTEFL_CONFIG.')

environment = 'test'
log.debug("Using config from %s", config_path)

with open(config_path) as f:
    db_config_str = f.read()
    db_config = json.loads(db_config_str)
    db_conn_str = db_config[environment]['db_connection_str']



