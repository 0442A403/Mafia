import logging
import time

from scheme.engine_pb2 import GetNotificationsRequest


def loop_notification_check(engine, session_id, user_key):
    for request in get_client_request(session_id, user_key):
        response = engine.GetNotifications(request)
        for notification in response.notifications:
            print(notification)

        time.sleep(0.5)


def get_client_request(session_id, user_key):
    while True:
        yield GetNotificationsRequest(session_id=session_id, user_key=user_key)