"""Views for Pyramid Learning Journal."""

from pyramid.response import Response

import io
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """Route user to list of all entries in LJ."""
    imported_text = io.open(os.path.join(HERE, '../templates/homepage.html')).read()
    return Response(imported_text)


def detail_view(request):
    """Route user to detailed entry in LJ."""
    imported_text = io.open(os.path.join(HERE, '../templates/detail-entry.html')).read()
    return Response(imported_text)


def create_view(request):
    """Route user to create entry page in LJ."""
    imported_text = io.open(os.path.join(HERE, '../templates/new-entry.html')).read()
    return Response(imported_text)


def update_view(request):
    """Route user to update entry page in LJ."""
    imported_text = io.open(os.path.join(HERE, '..templates/edit-entry.html')).read()
    return Response(imported_text)
