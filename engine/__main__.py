import __init__
from concurrent import futures
import grpc
from engine import Engine
from scheme import engine_pb2_grpc
import logging
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",
                        "--single",
                        type=bool,
                        default=False,
                        help="Make server running session with id 0 at start")
    parser.add_argument("-m",
                        "--max-player-number",
                        type=int,
                        help="Max player number. When it exceeded game starts automatically",
                        default=5)
    parser.add_argument("--default-mafia-count",
                        type=int,
                        help="Default mafia count in session",
                        default=1)
    parser.add_argument("--default-detective-count",
                        type=int,
                        help="Default detective count in session",
                        default=1)
    args = parser.parse_args()
    engine_args = {
        "default_mafia_count": args.default_mafia_count,
        "default_detective_count": args.default_detective_count,
    }
    if args.single:
        engine_args["single"] = args.single
    if args.max_player_number:
        if args.max_player_number == 0:
            args.max_player_number = None
        engine_args["max_players"] = args.max_player_number

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    engine_pb2_grpc.add_MafiaEngineServicer_to_server(Engine(**engine_args), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logging.info("Engine is started")
    server.wait_for_termination()
