from django.core.cache import cache

class ClearCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Очистка всего кэша
        cache.clear()
        response = self.get_response(request)
        return response