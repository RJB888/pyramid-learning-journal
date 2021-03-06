"""Test files for Pyramid Learning Journal."""

from __future__ import unicode_literals
from pyramid import testing
import pytest
from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden
import transaction
from robert_pyramid_learning_journal.models.mymodel import JournalEntry
from robert_pyramid_learning_journal.models.meta import Base


@pytest.fixture(scope='session')
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_journal'
    })
    config.include("robert_pyramid_learning_journal.models")
    config.include("robert_pyramid_learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def testdb(db_session):
    """."""
    new_entry = JournalEntry(title='new entry',
                             body='Was here.',
                             author='Joe',
                             date='11/1/18')
    db_session.add(new_entry)


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_response_title(dummy_request):
    """Test list view response of title."""
    from robert_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['title'] == 'Python 401 Learning Journal'


def test_list_view_response_is_a_dictionary(dummy_request):
    """Test that response to list_view is a dictionary."""
    from robert_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_response_has_good_img(dummy_request):
    """Test that response to list_view has the right image."""
    from robert_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['image'] == 'assault.jpg'


def test_after_entry_created_can_navigate_to_it(dummy_request, testdb):
    """."""
    from robert_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert response['title'] == 'new entry'


def test_list_view_response_has_a_post(dummy_request, testdb):
    """Test that response to list_view has the right image."""
    from robert_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['ljposts'][0].title == 'new entry'


def test_detail_view_has_correct_keys(dummy_request, testdb):
    """Test that response to detail_view has the correct keys."""
    from robert_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert 'image' in response
    assert 'ljpost' in response
    assert 'image' in response


def test_create_view_has_correct_response(dummy_request):
    """Test that response to create_view_has_correct routing."""
    from robert_pyramid_learning_journal.views.default import create_view
    dummy_request.matchdict['id'] = 4
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_new_entry_works_with_a_specific_entry(dummy_request):
    """Test that response to create_view has the correct value."""
    from robert_pyramid_learning_journal.views.default import create_view
    dummy_request.matchdict['id'] = 7
    response = create_view(dummy_request)
    assert response['image'] == 'scout.jpg'


def test_update_entry_works_for_response_title(dummy_request, testdb):
    """Test that response to update_view has the correct title."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 1
    response = update_view(dummy_request)
    assert response['ljpost'] == 'Was here.'


def test_update_entry_post_content_loads_correctly(dummy_request, testdb):
    """Test that response to update_view has the correct post."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 1
    response = update_view(dummy_request)
    assert response['image'] == 'saber.jpg'


from pyramid.config import Configurator


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    settings["sqlalchemy.url"] = 'postgres://localhost:5432/test_journal'
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()


@pytest.fixture
def testapp(request):
    """Build the testapp."""
    from webtest import TestApp
    app = main({})
    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def teardown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(teardown)

    return TestApp(app)


@pytest.fixture
def dbdata(testapp):
    """Handle database data with testapp."""
    from .models import get_tm_session
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add(JournalEntry(title='new entry', body='Was here.',
                                   author='Joe', date='11/1/18'))


def test_get_home_route_returns_200_status(testapp, dbdata):
    """Test that the home route returns a 200 ok status."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_http_not_found(testapp, dbdata):
    """Test call to detail view with bad index gives 404 error."""
    assert testapp.get('/journal/300', status=404)


def test_update_entry_raises_http_error(testapp, dbdata):
    """Test that response to update_view raises httperror."""
    assert testapp.get('/journal/-5/edit-entry', status=404)


def test_update_entry_raises_http_error_with_bad_index(testapp, dbdata):
    """Test that response to update_view with bad index raises http error."""
    assert testapp.get('/journal/-5/edit-entry', status=404)


# def test_create_view_redirects_to_home_on_success(testapp, dbdata):
#     """."""
#     testapp.post('/login', {
#         'username':"rjbronson",
#         'password':"flergtheblerg"
#         })
#     new_entry = {
#         "title":"New Entry",
#         "body": "some body words",
#         "author":"RJB",
#         "Date":"11/11/11"
#     }
#     response = testapp.post("/journal/new-entry", new_entry)
#     assert response.location == 'http://localhost6543/'

# def test_update_entry_raises_403_if_no_login(testapp):
#     """Test that response to update_view raises http 403 if not logged in."""
#     with pytest.raises(HTTPForbidden):
#         assert testapp.get('/journal/1/edit-entry')


# def test_create_entry_raises_403_if_no_login(testapp):
#     """Test that response to create_view raises http 403 if not logged in."""
#     assert testapp.get('/journal/new-entry', status=403)
