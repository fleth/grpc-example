import time
import grpc
from concurrent import futures

import person_pb2
import person_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class InfomationServicer(person_pb2_grpc.InfomationServicer):
    def Get(self, request, context):
        person = person_pb2.Person()
        person.id = 1234
        person.email = "jdoe@example.com"
        person.name = request.name
        return person

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_InfomationServicer_to_server(
        InfomationServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

serve()
