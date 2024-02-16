from prometheus_client import Counter, Gauge

# Counter for tracking the total number of requests.
REQUEST_COUNTER = Counter(
    'app_requests_total',
    'Total number of requests by method, endpoint, and response status',
    ['method', 'endpoint']
)

# Gauge for tracking the current mood of the user.
MOOD_CHECK = Gauge(
    'user_mood',
    'Current mood of the user',
    labelnames=['user']
)
