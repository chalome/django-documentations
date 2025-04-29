import time
from django.http import HttpResponseForbidden

class IPWhitelistMiddleware:
    ALLOWED_IPS = ['127.0.0.1', '192.168.1.100']  # Replace with your allowed IP addresses

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Access Denied: Your IP is not whitelisted.")
        return self.get_response(request)
    

class RateLimitMiddleware:
    RATE_LIMIT = 5  # Maximum number of requests allowed
    TIME_FRAME = 1 * 60  # Time frame in seconds (e.g., 1 hour)

    def __init__(self, get_response):
        self.get_response = get_response
        self.client_requests = {}

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        current_time = time.time()

        if ip_address in self.client_requests:
            requests, last_time = self.client_requests[ip_address]
            if current_time - last_time < self.TIME_FRAME:
                if requests >= self.RATE_LIMIT:
                    return HttpResponseForbidden("Rate limit exceeded. Try again later.")
                else:
                    self.client_requests[ip_address] = (requests + 1, last_time)
            else:
                self.client_requests[ip_address] = (1, current_time)
        else:
            self.client_requests[ip_address] = (1, current_time)

        return self.get_response(request)