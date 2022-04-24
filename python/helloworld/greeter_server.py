# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import math

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# For add new function:
#   1) add new rpc to helloworld.proto
#   2)NOTE: 
#      now we need to update the grpc code used by our application
#      to use the new service definition.
#      at examples/python/helloworld:
#      python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
#   3) add new function to greeter class <server code>.
#   4) update the client --> use the new function at the client <client code>. 

class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
    
    # add new fuction to server.
    def SayHelloAgain(self, request, context):
        # we can not send request only.
        # because the person should get at least name, family, id.
        return helloworld_pb2.Person(name=request.name, family=request.family, id=request.id)

    def Calculation(self, request, context):
        a = request.a
        b = request.b
        c = request.c
        delta = b * b - 4 * a * c
        x = []
        if delta > 0:
            x_1 = (-b + math.sqrt(delta))/(2*a)
            x_2 = (-b - math.sqrt(delta))/(2*a)
            x.append(str(x_1))
            x.append(str(x_2))           
        elif delta == 0:
            x_1 = -b/(2*a)
            x.append(str(x_1))
        else:
            x_1 = "NO ANSWER."
            x.append(x_1)
        
        return helloworld_pb2.Result(x = x)

    def Bidirec(self, request, context):
        return helloworld_pb2.HelloReply(message="hello, %s!" % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
