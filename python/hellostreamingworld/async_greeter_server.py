# Copyright 2021 gRPC authors.
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
"""The Python AsyncIO implementation of the GRPC hellostreamingworld.MultiGreeter server."""

import asyncio
from email import message
from lib2to3.pgen2.token import NUMBER
import logging
from secrets import randbits
import time
from tkinter import N
import random

import grpc
from hellostreamingworld_pb2 import HelloReply
from hellostreamingworld_pb2 import HelloRequest
from hellostreamingworld_pb2 import HelloReplyAgain
from hellostreamingworld_pb2_grpc import MultiGreeterServicer
from hellostreamingworld_pb2_grpc import add_MultiGreeterServicer_to_server

NUMBER_OF_REPLY = 10


class Greeter(MultiGreeterServicer):

    async def sayHello(self, request: HelloRequest,
                       context: grpc.aio.ServicerContext) -> HelloReply:
        logging.info("Serving sayHello request %s", request)
        # for i in range(NUMBER_OF_REPLY):
        #     yield HelloReply(message=f"Hello number {i}, {request.name}!")
        applications = [
            {"name": "chrome", "version": 1},
            {"name": "firefox", "version": 2},
            {"name": "idm", "version": 3},
            {"name": "player", "version": 4},
            {"name": "book", "version": 5},
        ]
        
        while True:
            index = random.randint(0, 4)
            delay = random.random()
            yield HelloReplyAgain(name=applications[index]['name'], version=applications[index]['version'])
            print("server for " + str(delay * 3) + " will shutdown.")
            time.sleep(delay * 3)
    
    async def sayHelloAgain(self, request: HelloRequest, context: grpc.aio.ServicerContext) -> HelloReply:
        logging.info("SERVING SAYHELLO REQUEST %s", request)

        while True:
            yield HelloReply(message="MESSAGE FROM SAYHELLOAGAIN!")
            time.sleep(3)



async def serve() -> None:
    server = grpc.aio.server()
    add_MultiGreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
