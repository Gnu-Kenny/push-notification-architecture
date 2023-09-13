from botocore.args import logger
from botocore.exceptions import ClientError


def send_single_message(queue, message_body: str):
    try:
        response = queue.send_message(
            MessageBody=message_body
        )
    except ClientError as error:
        logger.exception("Send message failed: %s", message_body)
        raise error
    else:
        return response
