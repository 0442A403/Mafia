import threading
import time

import redis


class Chat:
    def __init__(self, host, port, chat_id, username):
        self.host = host
        self.port = port
        self.chat_id = chat_id
        self.username = username
        self.redis = redis.Redis(host=host, port=port)
        self.is_alive = False
        self.chat_thread = None

    def chat_loop(self):
        subs = self.redis.pubsub()
        subs.subscribe(self.chat_id)

        while self.is_alive:
            message = subs.get_message()

            if message and message["type"] == "message":
                print(str(message["data"], 'utf8'))

            time.sleep(0.25)

        subs.unsubscribe()

    def start(self):
        self.is_alive = True
        self.chat_thread = threading.Thread(target=Chat.chat_loop, args=(self,))
        self.chat_thread.start()

    def stop(self):
        self.is_alive = False
        self.chat_thread.join()

    def send_message(self, message):
        self.redis.publish(self.chat_id, f"Message from {self.username}: {message}")


