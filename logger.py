import uuid
from logging import getLogger, FileHandler, Formatter



class MyLogger(object):
    def __init__(self, log_filename):
        self.log_format = '%(levelname)-8s [%(asctime)s] %(message)s'
        self.style_format = '%Y-%m-%d %H:%M:%S'

        self.file_handler = FileHandler('logs/{}.log'.format(log_filename))
        self.formatter = Formatter(self.log_format, self.style_format)
        self.file_handler.setFormatter(self.formatter)

        self.log = getLogger()
        self.log.addHandler(self.file_handler)

    def logger(self):
        return self.log
