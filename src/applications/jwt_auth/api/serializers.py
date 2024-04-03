from rest_framework import serializers

from applications.users.api.serializers import RetrieveUserSerializer


class TokenSerializer(serializers.Serializer):
    user = RetrieveUserSerializer(read_only=True)
    access = serializers.CharField()
    refresh = serializers.CharField()
