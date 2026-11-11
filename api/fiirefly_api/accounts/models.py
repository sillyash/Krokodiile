from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Arise data that doesn't fit on Django's User."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    )
    # Public name, the AriseID (username) stays admin-only.
    nickname = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'profil'

    def __str__(self):
        return self.nickname or self.user.get_username()
