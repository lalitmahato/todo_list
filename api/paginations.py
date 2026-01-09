from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class CustomPagination(PageNumberPagination):
    # Set the default page size
    page_size = 1

    # Allow the client to set the page size via a query param (e.g., ?page_size=20)
    page_size_query_param = 'page_size'

    # Set a maximum limit to prevent server overload
    max_page_size = 100

    def get_paginated_response(self, data):
        final_data = {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "total_pages": self.page.paginator.num_pages,  # The custom addition
            "results": data,
        }
        return Response(final_data, status=status.HTTP_200_OK)