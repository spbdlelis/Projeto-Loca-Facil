import threading
import socket
from ast import literal_eval

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):
        ack = None
        while True:
            packet = self.csocket.recv(6144).decode() 
            try:
                packet = literal_eval(packet)
                print(packet)
                ack = 1
                break
            except:
                pass
        message = {
            'status': 'success' if ack is not None else 'error'
        }
        print(message)
        self.csocket.send(str(message).encode())
        self.csocket.close()


if __name__ == '__main__':
    addr = ("", 7000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(10)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()


""" 
class Servidor():
    def __init__(self):
        host = 'localhost'  #Não possui IP pois é local
        port = 7001
        addr = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
        self.socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
        self.socket.listen(100)
        while(True):
            self.socket.accept()
            print("Nova conexão")
            user_thread = threading.Thread(target = receptor(self.socket))
            user_thread.start()
            user_thread.join()

def processador(mensagem):
    dado = literal_eval(mensagem)   #dicionário com o dado
    print(dado)
    #Gravar no banco

def receptor(socket):
    mensagem = socket.recv(1024).decode()
    processador = threading.Thread(target=processador(mensagem))
    processador.start()
    processador.join()


def aceitar(self):       
    while True:
        self.socket.accept()
        print("Nova Conexão")

Servidor() """
