
logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'log_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
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
        }
    },
    'loggers': {
        'debug_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'app_logger': {
            'level': 'WARNING',
            'handlers': ['file']
        }
    },
}