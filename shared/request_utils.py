from rest_framework.response import Response
import logging
logger = logging.getLogger("django")

def log_and_respond(data = None, message = None, message_code=None, status = None, exception=None):
    if exception is not None:
        logger.exception(exception)
    response_body = {
        "code" : status,
        "message_code" : message_code,
        "message" : message,
        "data" : data
    }

    return Response(response_body, status=status)