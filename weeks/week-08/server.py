import time
import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc


class SessionsService(service_pb2_grpc.SessionsServiceServicer):

    
    def GetSession(self, request, context):
        return service_pb2.SessionResponse(
            id=request.id,
            ip="127.0.0.1"
        )

    
    def Subscribe(self, request, context):
        for i in range(5):
            yield service_pb2.SessionResponse(
                id=request.id,
                ip=f"127.0.0.{i}"
            )
            time.sleep(1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SessionsServiceServicer_to_server(
        SessionsService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()