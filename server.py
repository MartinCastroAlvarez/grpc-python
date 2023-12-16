from concurrent import futures
import grpc
import schema_pb2
import schema_pb2_grpc


class Greeter(schema_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return schema_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
