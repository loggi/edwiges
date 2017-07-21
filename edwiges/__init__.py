"""Main entry point
"""
import os

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

def get_config_environ(name):
    env_name = name.replace('.', '_').upper()
    return os.environ.get(env_name)


def main(global_config, **settings):

    for name in ENV_SETTINGS:
        settings[name] = get_config_environ(name) or settings.get(name)
        
    for name in REQUIRED_SETTINGS:
        if name not in settings:
            error = 'confiration entry for {} is missing'.format(name)
            raise ConfigurationError(error)

    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("edwiges.views")

    return config.make_wsgi_app()
