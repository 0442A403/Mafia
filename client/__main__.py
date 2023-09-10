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
    args = parser.parse_args()
    bot_session_id = args.bot_session_id
    host = args.engine_host
    if bot_session_id is not None:
        client = MafiaClient(host, bot_session_id)
    else:
        client = Client(host)

    for command in client.next_command():
        if not command:
            continue
        if command[0] not in client.commands:
            print(f"Bad commands. You can use {list(client.commands.keys())}.")
            continue
        if len(command) != len(signature(client.commands[command[0]]).parameters):
            print("Bad number of arguments")
            continue

        client.commands[command[0]](client, *command[1:])

