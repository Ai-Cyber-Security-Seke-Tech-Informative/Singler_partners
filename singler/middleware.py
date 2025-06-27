# myproject/middleware.py

from django.http import HttpResponseNotFound

class BlockPathsMiddleware:
    BLOCKED_PATHS = [
        # add other paths you want to block
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if path in self.BLOCKED_PATHS:
            return HttpResponseNotFound('<h1>404 Not Found</h1>')

        response = self.get_response(request)
        return response
