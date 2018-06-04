import socket
import _thread
import addressbook_pb2
import sys
import numpy as np
#import pandas as pd


try:
  raw_input          # Python 2
except NameError:
  raw_input = input  # Python 3


def help():
    print("Hi there!\n")
    print("Usage:", sys.argv[0],"\n")
    sys.exit(-1)


HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 16785            # Porta que o Servidor esta
address_book = addressbook_pb2.AddressBook()

#Ia criar um dataframe pra trabalhar quase que
#completamente com operacoes em disco tornando muito eficiente consultas e operacoes como update e delete
#data = {'name':[],'id':[],'email':[],'phonetype':[],'phonenumber':[]}
#df = pd.DataFrame(data=d)

def readALL():
    with open('adresbok', "rb") as f:
        address_book.ParseFromString(f.read())


def delete(id):
    with open('adresbok', "rb") as f:
        address_book.ParseFromString(f.read())

def insert(msgs):
    with open('adresbok', "ab") as f:
        f.write(msgs)

def conectado(con, cliente):
    print ('Conectado por', cliente)
    
    while True:
        msg = con.recv(1024)
        if msg == b'1':
            proto = con.recv(1024)
            insert(proto)

        if not msg: break
        print (cliente, msg)

    print ('Finalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)

    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        _thread.start_new_thread(conectado, tuple([con, cliente]))

    tcp.close()

if len(sys.argv) != 1:
    help()
   
main()