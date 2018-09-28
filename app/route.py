# coding=utf-8
from __future__ import absolute_import

from app.link.api import LinkApi


restful_routes = {
    ('/links', '/links/<int:id>'): LinkApi
}


def register_route(api):
    for route, resource in restful_routes.iteritems():
        if isinstance(route, (tuple, list)):
            api.add_resource(resource, *list(route))
        else:
            api.add_resource(resource, route)
