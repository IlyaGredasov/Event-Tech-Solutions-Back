from typing import cast

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from dj_rest_auth.views import LoginView, UserDetailsView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken

from applications.jwt_auth.api.serializers import TokenSerializer


AUTH_TAG = 'Авторизация'


class CustomLoginView(LoginView):

    def login(self):
        self.user = self.serializer.validated_data['user']

        self.token = cast(RefreshToken, RefreshToken.for_user(self.user))

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        return Response(
            data=self.get_response_serializer()(
                instance={
                    'user': self.user,
                    'access': self.token.access_token,
                    'refresh': self.token
                },
                context=self.get_serializer_context(),
            ).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            status.HTTP_200_OK: TokenSerializer,
        },
        tags=[AUTH_TAG],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomUserDetailsView(UserDetailsView):
    @extend_schema(
        tags=[AUTH_TAG],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=[AUTH_TAG],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)