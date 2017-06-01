import logging
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
log_name = 'smartefl'

log = logging.getLogger(log_name)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s - %(levelname)s - %(message)s')

# fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh)
log.addHandler(ch)