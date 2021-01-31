
import logging

def set_custom_log_info(file_name):
    logging.basicConfig(filename=file_name, level=logging.INFO)

def report(e:Exception):
    logging.exception(str(e))
