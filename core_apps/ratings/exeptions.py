from rest_framework.exceptions import APIException


class YouHaveAlreadyRated(APIException):
    status_code = 403
    default_detail = "you already rated this article"
    default_code = "bad_request"
