"""Routes for Learning Journal."""


def includeme(config):
    """Routes."""
    config.add_static_view('static', 'robert_pyramid_learning_journal:static')
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new-entry')
    config.add_route('update_view', '/journal/{id:\d+}/edit-entry')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')