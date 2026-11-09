"""Arise Connect OAuth client (https://connect.iiens.net)."""

from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Profile

ARISE = settings.ARISE

oauth = OAuth()
oauth.register(
    name='arise',
    client_id=ARISE['CLIENT_ID'],
    client_secret=ARISE['CLIENT_SECRET'],
    issuer=ARISE['ISSUER'],
    authorize_url=f'{ARISE["ISSUER"]}/oauth2/auth',
    access_token_url=f'{ARISE["ISSUER"]}/oauth2/token',
    userinfo_endpoint=f'{ARISE["ISSUER"]}/userinfo',
    # Keys used to verify the ID token returned with the `openid` scope.
    jwks_uri=f'{ARISE["ISSUER"]}/.well-known/jwks.json',
    client_kwargs={
        'scope': ARISE['SCOPES'],
        'code_challenge_method': 'S256',
        'token_endpoint_auth_method': 'client_secret_basic',
    },
)

arise = oauth.create_client('arise')


def user_from_userinfo(info):
    """Create or update the local user matching an Arise userinfo payload."""
    # `id` is the AriseID (e.g. dupontj2042), `sub` may be obfuscated.
    username = info.get('id') or info['sub']
    user, created = get_user_model().objects.get_or_create(username=username)
    if created:
        user.set_unusable_password()
        user.save(update_fields=['password'])
    nickname = info.get('preferred_nickname') or info.get('nickname') or ''
    Profile.objects.update_or_create(user=user, defaults={'nickname': nickname})
    return user


def display_name(user):
    """Public name: Arise nickname, falling back to the AriseID."""
    profile = getattr(user, 'profile', None)
    return (profile and profile.nickname) or user.get_username()
