from django.contrib.auth.models import User
from social.exceptions import AuthException


def create_or_update_user(backend, details, user=None, *args, **kwargs):
    print('create_or_update_user (backend=%s, details=%s, user=%s, args=%s, kwargs=%s)' % (backend, details, user, args, kwargs))
    if user:
        return None

    username = details.get('username')
    if username:
        users = list(User.objects.filter(username__iexact=username))
        if len(users) == 0:
            return None
        elif len(users) > 1:
            raise AuthException(backend,'The given username is associated with another account')
        else:
            return {'user': users[0], 'is_new': False}
