import os
import logging
from datetime import datetime
'''
This is a simple wrapper module to specify a global logging
configuration for other modules to import.
'''
now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
# log_location = os.getenv('SMARTEFL_LOG')
log_name = 'smartefl'

log_name_date = log_name + "_" + now

# if log_location is not None:
#     log_and_path = os.path.join(log_location, log_name_date)
# else:
#     log_and_path = log_name_date

log = logging.getLogger(log_name)
log.setLevel(logging.DEBUG)

# log_and_path += ".log"

# fh = logging.FileHandler(log_and_path)
# fh.setLevel(logging.DEBUG)

# console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s - %(levelname)s - %(message)s')

# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh)
log.addHandler(ch)