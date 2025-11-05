from rest_framework.pagination import PageNumberPagination

class DefaultPaginition(PageNumberPagination):
    page_size = 10
