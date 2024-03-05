from socket import *  
import sqlite3

def selectDB1():
	conn = sqlite3.connect('database.db')
	print ("Opened database successfully")
	cursor = conn.execute("SELECT pergunta, opcaoA, opcaoB, opcaoC, opcaoD, resposta from PERGUNTAS WHERE id=1")
	for row in cursor:
		pergunta=row[0]
		opcaoA=row[1]
		opcaoB=row[2]
		opcaoC=row[3]
		opcaoD=row[4]
		resposta=row[5]
	conn.close()
	return pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta

def selectDB2():
	conn = sqlite3.connect('database.db')
	print ("Opened database successfully")
	cursor = conn.execute("SELECT pergunta, opcaoA, opcaoB, opcaoC, opcaoD, resposta from PERGUNTAS WHERE id=2")
	for row in cursor:
		pergunta=row[0]
		opcaoA=row[1]
		opcaoB=row[2]
		opcaoC=row[3]
		opcaoD=row[4]
		resposta=row[5]
	conn.close()
	return pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta


serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
#atribui a porta ao socket criado
serverSocket.bind(('', serverPort))    
#aceita conexoes 
#com no maximo um cliente na fila 
serverSocket.listen(1)
pergunta1,opcaoA1,opcaoB1,opcaoC1,opcaoD1,resposta1 = selectDB1()
pergunta1=pergunta1+'? \n a) '+opcaoA1+'\n b) '+opcaoB1+'\n c) '+opcaoC1+'\n d) '+opcaoD1
pergunta2,opcaoA2,opcaoB2,opcaoC2,opcaoD2,resposta2 = selectDB2()
pergunta2=pergunta2+'? \n a) '+opcaoA2+'\n b) '+opcaoB2+'\n c) '+opcaoC2+'\n d) '+opcaoD2
while True:
	connectionSocket, addr = serverSocket.accept()
	connectionSocket.send(pergunta1.encode())     
	data1 = connectionSocket.recv(1024)
	data1=data1.decode()
	connectionSocket.send(pergunta2.encode())     
	data2 = connectionSocket.recv(1024)
	data2=data2.decode()
	   
	if(data1==resposta1):
		mensagem="Pergunta 1 correta."
		connectionSocket.send(mensagem.encode())
	else:
		mensagem="Pergunta 1 incorreta, a resposta era a letra: "
		connectionSocket.send(mensagem.encode())
		connectionSocket.send(resposta1.encode())
	
	if(data2==resposta2):
		mensagem="\nPergunta 2 correta."
		connectionSocket.send(mensagem.encode())
	else:
		mensagem="\nPergunta 2 incorreta, a resposta era a letra: "
		connectionSocket.send(mensagem.encode())
		connectionSocket.send(resposta2.encode())

	connectionSocket.close()