from rest_framework import status
from rest_framework.response import Response


class BaseServiceException(Exception):
    detail = 'Ошибка обработки данных'

    def __init__(self, detail=None):
        self.detail = detail or self.detail


class PermissionDeniedException(BaseServiceException):
    detail = 'Ошибка! Недостаточно прав для выполнения данного действия'


def handle_service_exception(exc: BaseServiceException):
    if isinstance(exc, PermissionDeniedException):
        return Response(
            data={'detail': exc.detail},
            status=status.HTTP_403_FORBIDDEN,
        )
    return Response(
        data={'detail': exc.detail},
        status=status.HTTP_400_BAD_REQUEST,
    )
