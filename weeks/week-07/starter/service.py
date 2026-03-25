import grpc
from concurrent import futures

import service_pb2
import service_pb2_grpc



invoices_db = []



class ServiceImplementation(service_pb2_grpc.InvoicesServiceServicer):

    def CreateInvoice(self, request, context):
        new_invoice = {
            "id": len(invoices_db) + 1,
            "name": request.name,
            "amount": request.amount
        }

        invoices_db.append(new_invoice)

        return service_pb2.CreateInvoiceResponse(
            id=new_invoice["id"],
            name=new_invoice["name"],
            amount=new_invoice["amount"]
        )



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    service_pb2_grpc.add_InvoicesServiceServicer_to_server(
        ServiceImplementation(), server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("gRPC server started on port 50051")

    server.wait_for_termination()


if __name__ == '__main__':
    serve()