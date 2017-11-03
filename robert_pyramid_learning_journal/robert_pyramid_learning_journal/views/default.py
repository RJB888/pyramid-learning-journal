"""Create callables for calling routes."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound

FMT = "%m/%d/%Y"

POST = [
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Robert Mother-Effin Bronson',
     'body': 'I am the baddest sith on the block.', 'id': 1},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Robert Mother-Effin Bronson',
     'body': 'I am the baddest sith on the block.', 'id': 2},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Robert Mother-Effin Bronson',
     'body': 'I am the baddest sith on the block.', 'id': 3},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Robert Mother-Effin Bronson',
     'body': 'I am the baddest sith on the block.', 'id': 4},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Robert Mother-Effin Bronson',
     'body': 'I am the baddest sith on the block.', 'id': 5},
]


@view_config(route_name='list_view',
             renderer='robert_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    return {'ljposts': POST,
            'title': 'Robert Bronson, Learning Journal',
            'image': "home-bg.jpg"}


@view_config(route_name='detail_view',
             renderer='robert_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    # if post_id not in POST:
    for post in POST:
        if post['id'] == post_id:
            return {'ljpost': post,
                    'title': post.title,
                    'image': 'post-bg.jpg'}
    raise HTTPNotFound


@view_config(route_name='create_view',
             renderer='robert_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    # does anything go here??
    return {'title': 'Create New Entry',
            'image': 'new-entry.jpg'}


@view_config(route_name='update_view',
             renderer='robert_pyramid_learning_journal:templates/templates/edit-entry.jinja2')
def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    if post_id not in POST:
        return HTTPNotFound
    for post in POST:
        if post['id'] == post_id:
            return {'ljposts': post,
                    'title': 'Update Entry',
                    'image': 'post-bg.jpg'}