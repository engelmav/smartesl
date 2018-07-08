import os
import json
from logger import log


is_ci_build = os.getenv('CI_BUILD')

if is_ci_build == None:
    config_path = os.getenv('SMARTEFL_CONFIG')

    if config_path is None:
        raise RuntimeError('You must specify your config file path'
                        ' by setting SMARTEFL_CONFIG.')

    environment = 'test'
    log.debug("Using config from %s", config_path)

    with open(config_path) as f:
        config_str = f.read()
        config_json = json.loads(config_str)
        db_conn_str = config_json[environment]['db_connection_str']
else:
    log.debug("Initializing in CI pipeline")
    db_conn_str = "postgresql://localhost/travis_ci_test"