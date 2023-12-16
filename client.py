import grpc
import schema_pb2
import schema_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = schema_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(schema_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()

