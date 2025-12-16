from django.utils.timezone import now
from datetime import timedelta

def is_user_online(profile):
    return now() - profile.last_seen < timedelta(seconds=10)
