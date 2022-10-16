
logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'log_format': {
            'format': '{asctime} - {levelname} - module: {module} - function: {funcName} - {message}',
            'style': '{'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'log_format'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': "opencart_tests_log.log",
            'level': 'WARNING',
            'formatter': 'log_format'
        },
        # 'email': {
        #     'class': 'logging.handlers.SMTPHandler',
        #     'mailhost': '',
        #     'fromaddr': '',
        #     'toaddrs': '',
        #     'credentials': '',
        #     'subject': 'Houston, we have a problem',
        #     'level': 'CRITICAL',
        #     'formatter': 'log_format'
        # },
    },
    'loggers': {
        'logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
    },
}