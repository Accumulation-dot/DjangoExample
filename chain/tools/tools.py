from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30
    page_query_param = 'page'
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        next_link = self.get_next_link()
        next_response = '0'
        if next_link:
            next_response = '1'
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', next_response),
            ('list', data)
        ]))


def request_error(errors, r_status=status.HTTP_400_BAD_REQUEST):
    return Response(data=errors, status=r_status)
