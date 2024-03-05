import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute("INSERT INTO PERGUNTAS (pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta) \
      VALUES ('Qual e a capital do Brasil','Sao Paulo','Rio de Janeiro','Brasilia','Florianopolis','c')");

conn.execute("INSERT INTO PERGUNTAS (pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta) \
      VALUES ('Onde foi inventando o chuveiro eletrico','Franca','Inglaterra','Italia','Brasil','d')");

conn.execute("INSERT INTO PERGUNTAS (pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta) \
      VALUES ('Qual o maior pais do mundo','Russia','China','Canada','Estados Unidos','a')");

conn.execute("INSERT INTO PERGUNTAS (pergunta,opcaoA,opcaoB,opcaoC,opcaoD,resposta) \
      VALUES ('Quem inventou a lampada eletrica','Isac Newton','Thomas Edison','Cristovao Colombo','Albert Einstein','b')");

conn.commit()
print ("Records created successfully")
conn.close()