from __future__ import annotations

from fastapi import status


class BaseAPIException(Exception):
    status_code: int
    error_code: str = ""
    default_message: str = ""

    def __init__(self, status_code: int = 400, default_message: str = "error"):
        if status:
            self.status_code = status_code
        if default_message:
            self.default_message = default_message


# 400
class CannotBeDeleted(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "CANNOT_BE_DELETED"
    default_message = "Cannot be deleted because the data is linked"


class DataDoesNotExist(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "DATA_DOES_NOT_EXIST"
    default_message = "Data with the specified ID does not exist"


class ParameterError(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "PARAMETER_ERROR"
    default_message = "Parameter error"


# 422
class DuplicateError(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = "DUPLICATE_ERROR"
    default_message = "Duplicate Error"


# 401
class IncorrectUsernameOrPassword(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INCORRECT_USERNAME_OR_PASSWORD"
    default_message = "Incorrect username or password"


class InvalidRefreshToken(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INVALID_REFRESH_TOKEN"
    default_message = "invalid refresh token"


class InvalidCredentials(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = "INVALID_CREDENTIALS"
    default_message = "INVALID_CREDENTIALS"


# 403
class PermissionDenied(BaseAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    error_code = "PERMISSION_DENIED"
    default_message = "permission denied"


# 404
class NotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    error_code = "NOT_FOUND"
    default_message = "not found"


# 500
class InternalServerError(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_code = "INTERNAL_SERVER_ERROR"
    default_message = "internal server error"


class QueryDataError(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_code = "QUERY_DATA_ERROR"
    default_message = "QUERY_DATA_ERROR"
