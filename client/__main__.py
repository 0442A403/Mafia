import __init__
from client import Client
import argparse
from inspect import signature
from mafia_client import MafiaClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--bot-session-id",
        type=str,
        default=False,
        help="if defined it starts bot client and connect to specified session-id"
    )
    parser.add_argument(
        "--engine-host",
        type=str,
        help="Address of engine",
        default="127.0.0.1:50051"
    )
    parser.add_argument(
        "--chat-host",
        type=str,
        help="Address of chat redis",
        default="127.0.0.1"
    )
    parser.add_argument(
        "--chat-port",
        type=int,
        help="Port of chat redis",
        default=6379
    )
    args = parser.parse_args()

    bot_session_id = args.bot_session_id
    host = args.engine_host
    chat_host = args.chat_host
    chat_port = args.chat_port

    if bot_session_id:
        client = MafiaClient(bot_session_id, host, chat_host, chat_port)
    else:
        client = Client(host, chat_host, chat_port)

    for command, source in client.next_command():
        if not command:
            continue

        if command[0] == "chat":
            if len(command) == 0:
                print("Bad number of arguments")
                continue
            client.send_message(source[source.find(command[1]):])
            continue

        if command[0] not in client.commands:
            print(f"Bad commands. You can use {list(client.commands.keys())}.")
            continue
        if len(command) != len(signature(client.commands[command[0]]).parameters):
            print("Bad number of arguments")
            continue

        client.commands[command[0]](client, *command[1:])

