from rest_framework.exceptions import APIException


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "ypu cant follow yourself"
    default_code = "forbidden"
