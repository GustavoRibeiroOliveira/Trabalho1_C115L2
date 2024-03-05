import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT id, pergunta, opcaoA, opcaoB, opcaoC, opcaoD, resposta from PERGUNTAS")
for row in cursor:
   print ("ID = ", row[0])
   print ("Pergunta = ", row[1])
   print ("Opção A = ", row[2])
   print ("Opção B = ", row[3])
   print ("Opção C = ", row[4])
   print ("Opção D = ", row[5])
   print ("resposta = ", row[6], "\n")

print ("Operation done successfully")
conn.close()