from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import cookie_standsSerializer


class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = cookie_standsSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = cookie_standsSerializer
