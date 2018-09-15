import person_pb2
import sys

person = person_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phone.add()
phone.number = "555-4321"
phone.type = person_pb2.Person.HOME

print(person.SerializeToString())
