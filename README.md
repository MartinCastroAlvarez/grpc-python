# grpc-python
gRPC server &amp; client using Python

![wallpaper.png](./wallpaper.png)

gRPC is an open-source remote procedure call (RPC) framework initially developed by Google, which enables efficient and easy communication between servers and clients in different environments. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features like authentication, load balancing, and efficient connection management. gRPC is language-agnostic, offering scalable and high-performance communication particularly suited for microservices architecture. Its design allows developers to define clear service contracts, simplifying the process of connecting systems across languages and platforms. This makes gRPC an ideal choice for building distributed systems and services that require efficient, low-latency communication, such as real-time data processing and cloud-native applications.

## Instructions

Generate gRPC files:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. your_service.proto
```

Start the server:

```bash
python3 server.py
```

Start the client:

```bash
python3 client.py
```
