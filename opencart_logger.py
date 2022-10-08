import logging.config
from logging_settings import logger_config


class Logger:

    loggers = []

    @property
    def logger(self):
        if not self.loggers:
            logging.config.dictConfig(logger_config)
            l = logging.getLogger('logger')
            self.loggers.append(l)
        return self.loggers[0]

