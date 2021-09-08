from rest_framework import serializers
from .models import CookieStand


class cookie_standsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        fields = "__all__"
