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
                        help="Max player number. When it exceeded game starts automatically")
    args = parser.parse_args()
    engine_args = {}
    if args.single:
        engine_args["single"] = args.single
    if args.max_player_number:
        engine_args["max_players"] = args.max_player_number

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    engine_pb2_grpc.add_MafiaEngineServicer_to_server(Engine(**engine_args), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logging.info("Engine is started")
    server.wait_for_termination()
