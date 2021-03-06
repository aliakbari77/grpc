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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import time
from urllib import response
import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name=input("enter your name: ")))
        # print("Greeter client received: " + response.message)

        # use the new funtion that defined at server
        # name = input("enter your name: ")
        # family = input("enter your family: ")
        # id = int(input("enter your id: "))
        # response = stub.SayHelloAgain(helloworld_pb2.Person(name=name, family=family, id=id))
        # print("-------\nRESPONSE FROM SERVER:\n" + str(response))

        # use the calculation function that defined at server
        # while True:
        #     response = stub.Calculation(helloworld_pb2.Factor(a = 1, b = -11, c = 30))
        #     print(response)
        #     time.sleep(3)

        response = stub.listApplications(helloworld_pb2.ListSoftware(ids=["1"], type=1, clientUUID="clientUUID"))
        print(response)


        


if __name__ == '__main__':
    logging.basicConfig()
    run()
