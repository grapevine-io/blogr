from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('somesecret')
    authorization_policy = ACLAuthorizationPolicy()
    with Configurator(settings=settings,
                      authentication_policy=authentication_policy,
                      authorization_policy=authorization_policy) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.add_route('blog_action', '/blog/{action}',
                         factory='pyramid_blogr.security.BlogRecordFactory')
        config.scan()
    return config.make_wsgi_app()
