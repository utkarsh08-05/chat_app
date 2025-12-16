from django.utils.timezone import now

class LastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            profile = request.user.profile
            profile.last_seen = now()
            profile.save(update_fields=["last_seen"])

        return response
