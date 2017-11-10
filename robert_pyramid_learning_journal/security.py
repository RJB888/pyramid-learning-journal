"""."""
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def includme(config):
    """Set security config."""
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512')
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authz_policy)

def isauthenticated(username, password):
    """Verify proper username and password."""
    return username == os.environ.get('AUTH_USERNAME', '') and password == os.environ.get('AUTH_PASSWORD','')