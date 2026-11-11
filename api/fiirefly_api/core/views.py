from rest_framework import mixins, permissions, viewsets
from rest_framework.throttling import ScopedRateThrottle

from fiirefly_api.accounts.arise import display_name

from .models import LivreDorEntry, Soiree
from .serializers import LivreDorEntrySerializer, SoireeSerializer


class SoireeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Soiree.objects.all()
    serializer_class = SoireeSerializer


class LivreDorEntryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = LivreDorEntry.objects.all()
    serializer_class = LivreDorEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'livre-dor'

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(auteur=user, nom=display_name(user)[:50])
