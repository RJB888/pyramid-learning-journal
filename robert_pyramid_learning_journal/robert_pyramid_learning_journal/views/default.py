"""Views for Pyramid Learning Journal."""

from pyramid.response import Response

import io
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """Route user to list of all entries in LJ."""
    path = os.path.join(HERE, '../templates/homepage.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def detail_view(request):
    """Route user to detailed entry in LJ."""
    path = os.path.join(HERE, '../templates/detail-entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def create_view(request):
    """Route user to create entry page in LJ."""
    path = os.path.join(HERE, '../templates/new-entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def update_view(request):
    """Route user to update entry page in LJ."""
    path = os.path.join(HERE, '../templates/edit-entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())
