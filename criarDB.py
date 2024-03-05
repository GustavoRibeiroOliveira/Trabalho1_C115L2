import sqlite3

conn = sqlite3.connect('database.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE  PERGUNTAS(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        pergunta TEXT NOT NULL,
        opcaoA TEXT NOT NULL,
        opcaoB TEXT NOT NULL,
        opcaoC TEXT NOT NULL,       
        opcaoD TEXT NOT NULL,
        resposta TEXT NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()