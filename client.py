from socket import *   
serverName = 'localhost'
serverPort = 3000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

pergunta1 = clientSocket.recv(1024).decode()
print(pergunta1)

resposta1 = input("->")

clientSocket.send(resposta1.encode())

pergunta2 = clientSocket.recv(1024).decode()
print(pergunta2)

resposta2 = input("->")

clientSocket.send(resposta2.encode())

mensagem = clientSocket.recv(1024).decode()
print(mensagem)
mensagem = clientSocket.recv(1024).decode()
print(mensagem)

mensagem = clientSocket.recv(1024).decode()
print(mensagem)
mensagem = clientSocket.recv(1024).decode()
print(mensagem)

clientSocket.close()