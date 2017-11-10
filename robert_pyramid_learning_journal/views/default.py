"""Create callables for calling routes."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from robert_pyramid_learning_journal.models.mymodel import JournalEntry
from robert_pyramid_learning_journal.security import isauthenticated
from pyramid.security import remember

FMT = "%m/%d/%Y"


@view_config(route_name='list_view',
             renderer='robert_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    j_entries = request.dbsession.query(JournalEntry).order_by(JournalEntry.date.desc()).all()
    return {'ljposts': j_entries,
            'title': 'Python 401 Learning Journal',
            'image': "assault.jpg"}


@view_config(route_name='detail_view',
             renderer='robert_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    entry = request.dbsession.query(JournalEntry).get(post_id)
    return {'ljpost': entry,
            'title': entry.title,
            'image': 'patrol.jpg'}
    raise HTTPNotFound


@view_config(route_name='create_view',
             renderer='robert_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    # does anything go here??

    if request.method == "GET":
            return {'title': 'Create New Entry',
                    'image': 'scout.jpg'}

    if request.method == "POST":
        if not all([field in request.POST for field in ['Title',
                                                        'Journal Body']]):
            raise HTTPBadRequest
        new_post = JournalEntry(
            title=request.POST['Title'],
            body=request.POST['Journal Body'],
        )
        request.dbsession.add(new_post)
        return HTTPFound(request.route_url('list_view'))


@view_config(route_name='update_view',
             renderer='robert_pyramid_learning_journal:templates/edit-entry.jinja2')
def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    entry = request.dbsession.query(JournalEntry).get(post_id)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return {'ljpost': entry.body,
                'title': entry.title,
                'image': 'saber.jpg'}

    if request.method == "POST":
        if not all([field in request.POST for field in ['Title',
                                                        'Journal Body']]):
            raise HTTPBadRequest
        entry.title = request.POST['Title'],
        entry.body = request.POST['Journal Body'],
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=post_id))


@view_config(route_name='login', renderer='robert_pyramid_learning_journal:templates/login.jinja2')
def login(request):
    if request.method == "GET":
        return {'image': 'oriental.jpg'}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if isauthenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('list_view'), headers=headers)
        return {'image': 'oriental.jpg'}
