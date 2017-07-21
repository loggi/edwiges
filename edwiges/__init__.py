"""Main entry point
"""
import os
import logging

import logmatic
from pyramid.config import Configurator, ConfigurationError



REQUIRED_SETTINGS = [
    'edwiges.provider_host',
    'edwiges.provider_port',
]

ENV_SETTINGS = [
    'edwiges.provider_host',
    'edwiges.provider_port',
    'edwiges.provider_username',
    'edwiges.provider_password',
]


logger = logging.getLogger('edwiges')
handler = logging.StreamHandler()
handler.setFormatter(logmatic.JsonFormatter())

logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_config_environ(name):
    env_name = name.replace('.', '_').upper()
    return os.environ.get(env_name)


def main(global_config, **settings):

    for name in ENV_SETTINGS:
        settings[name] = get_config_environ(name) or settings.get(name)
        
    for name in REQUIRED_SETTINGS:
        if name not in settings:
            error = 'confiration entry for {} is missing'.format(name)
            logger.critical(error)
            raise ConfigurationError(error)

    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("edwiges.views")

    host = settings['edwiges.provider_host']
    port = settings['edwiges.provider_port']

    logger.info("Starting server", extra={'host': host, 'port': port})
    return config.make_wsgi_app()
