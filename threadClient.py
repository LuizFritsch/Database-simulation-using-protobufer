#! /usr/bin/env python


import addressbook_pb2
import sys
import socket
#import SistemaLocacao_pb2


#Pra compilar o .proto:
#protoc --python_out=. addressbook.proto


try:
  raw_input          # Python 2
except NameError:
  raw_input = input  # Python 3


# This function fills in a Person message based on user input.
def PromptForAddress(person):
  person.id = int(raw_input("Enter person ID number: "))
  person.name = raw_input("Enter name: ")

  email = raw_input("Enter email address (blank for none): ")
  if email != "":
    person.email = email

  while True:
    number = raw_input("Enter a phone number (or leave blank to finish): ")
    if number == "":
      break

    phone_number = person.phones.add()
    phone_number.number = number

    type = raw_input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = addressbook_pb2.Person.MOBILE
    elif type == "home":
      phone_number.type = addressbook_pb2.Person.HOME
    elif type == "work":
      phone_number.type = addressbook_pb2.Person.WORK
    else:
      print("Unknown phone type; leaving as default value.")


def help():
	print("Usage:", sys.argv[0])
	sys.exit(-1)

if len(sys.argv) != 1:
	help()

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 16785            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
def menu():
  print ('\n\n\n\n\n\n\n\n\n\n\nto exit, just type exit')
  print ('\nThis is version 1.0\n')
  print ('\nJust insert operation is workin and not the way it should... \n')
  print ('\n1.insert\n2.delete\n3.select\n')
  msg = raw_input()
  return msg
msg = menu()
while msg != 'exit':
	address_book = addressbook_pb2.AddressBook()
	if msg == '1':
		tcp.send(b'1')
		PromptForAddress(address_book.people.add())
		tcp.send(address_book.SerializeToString())
		print('\n\n\nEnviado!\n\n\n')
		msg=''
	if msg == '2':
		tcp.send(b'2')
		print('person ID: ')
		id = raw_input()
		tcp.send(b'')
		msg=''
	msg = menu()
tcp.close()
