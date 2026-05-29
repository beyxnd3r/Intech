import grpc
from concurrent import futures


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:8131")
    server.start()
    print("gRPC running on port 8131...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
