from authlib.integrations.base_client import OAuthError
from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_GET, require_POST

from .arise import arise, display_name, user_from_userinfo

NEXT_SESSION_KEY = 'arise_next'


def frontend_redirect(path='/'):
    """Redirect to a frontend route (the frontend uses hash routing)."""
    return HttpResponseRedirect(f'{settings.FRONTEND_URL}#{path}')


def safe_next(value):
    # Only plain frontend paths, never another host.
    if value and value.startswith('/') and not value.startswith('//'):
        return value
    return '/'


@require_GET
def login_view(request):
    request.session[NEXT_SESSION_KEY] = safe_next(request.GET.get('next'))
    return arise.authorize_redirect(request, settings.ARISE['REDIRECT_URI'])


@require_GET
def callback_view(request):
    next_path = request.session.pop(NEXT_SESSION_KEY, '/')
    try:
        token = arise.authorize_access_token(request)
        info = arise.userinfo(token=token)
    except OAuthError:
        return frontend_redirect()
    login(request, user_from_userinfo(info))
    return frontend_redirect(next_path)


@require_POST
def logout_view(request):
    logout(request)
    return HttpResponse(status=204)


@require_GET
def me_view(request):
    user = request.user
    data = None
    if user.is_authenticated:
        data = {'id': user.pk, 'username': user.get_username(), 'name': display_name(user)}
    return JsonResponse({'user': data, 'csrfToken': get_token(request)})
