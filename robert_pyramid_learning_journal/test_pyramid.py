"""Test files for Pyramid Learning Journal."""

from __future__ import unicode_literals
from pyramid import testing
import pytest
from pyramid.httpexceptions import HTTPNotFound


@pytest.fixture
def dummy_request():
    """Create dummy request fixture."""
    return testing.DummyRequest()



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


def test_list_view_response_has_a_post(dummy_request):
    """Test that response to list_view has the right image."""
    from robert_pyramid_learning_journal.views.default import list_view
    from robert_pyramid_learning_journal.data.lj_entries import ENTRIES
    response = list_view(dummy_request)
    assert response['ljposts'] == ENTRIES


def test_detail_view_has_correct_keys(dummy_request):
    """Test that response to detail_view has the correct keys."""
    from robert_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert 'image' in response
    assert 'ljpost' in response
    assert 'image' in response


def test_http_not_found(dummy_request):
    """Test that response to detail_view has the correct keys."""
    from robert_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = -10
    with pytest.raises(HTTPNotFound):
        assert detail_view(dummy_request)


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


def test_update_entry_works_for_response_title(dummy_request):
    """Test that response to update_view has the correct title."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 10
    response = update_view(dummy_request)
    assert response['title'] == 'Day 10  Brain cleanup?'


def test_update_entry_post_content_loads_correctly(dummy_request):
    """Test that response to update_view has the correct post."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 12
    response = update_view(dummy_request)
    assert response['image'] == 'saber.jpg'


def test_update_entry_raises_http_error(dummy_request):
    """Test that response to update_view raises httperror."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 5000
    with pytest.raises(HTTPNotFound):
        assert update_view(dummy_request)


def test_update_entry_error_type(dummy_request):
    """Test that httperror is 404."""
    from robert_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 2345
    with pytest.raises(HTTPNotFound):
        request = update_view(dummy_request)
        request.response.status = 404