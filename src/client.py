import grpc
import person_pb2
import person_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = person_pb2_grpc.InfomationStub(channel)

params = person_pb2.Params()
params.name = "test"

person_future = stub.Get.future(params)
person = person_future.result()

print(person)
