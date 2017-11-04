"""Create callables for calling routes."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from ..data.lj_entries import ENTRIES


FMT = "%m/%d/%Y"


@view_config(route_name='list_view',
             renderer='robert_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    return {'ljposts': ENTRIES,
            'title': 'Python 401 Learning Journal',
            'image': "assault.jpg"}


@view_config(route_name='detail_view',
             renderer='robert_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    for post in ENTRIES:
        if post['id'] == post_id:
            return {'ljpost': post,
                    'title': post['title'],
                    'image': 'patrol.jpg'}

    raise HTTPNotFound


@view_config(route_name='create_view',
             renderer='robert_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    # does anything go here??
    return {'title': 'Create New Entry',
            'image': 'scout.jpg'}


@view_config(route_name='update_view',
             renderer='robert_pyramid_learning_journal:templates/edit-entry.jinja2')
def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    # get post ID from detail_view page... import it?
    # do same filter fn from detail_view
    post_id = int(request.matchdict['id'])
    for post in ENTRIES:
        if post['id'] == post_id:
            return {'ljpost': post['body'],
                    'title': post['title'],
                    'image': 'saber.jpg'}

    raise HTTPNotFound
