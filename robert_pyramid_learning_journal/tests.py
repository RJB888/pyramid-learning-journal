"""Tests for pyramid."""

from pyramid.testing import DummyRequest
from pyramid.response import Response

from .views.default import list_view
from .views.default import detail_view
from .views.default import create_view
from .views.default import update_view


def test_list_view_returns_response():
    """Test list view."""
    req = DummyRequest()
    response = list_view(req)
    assert isinstance(response, Response)


def test_detail_view_returns_response():
    """Test detail view."""
    req = DummyRequest()
    response = detail_view(req)
    assert isinstance(response, Response)


def test_create_view_returns_response():
    """Test create view."""
    req = DummyRequest()
    response = create_view(req)
    assert isinstance(response, Response)


def test_update_view_returns_response():
    """Test update view."""
    req = DummyRequest()
    response = update_view(req)
    assert isinstance(response, Response)
