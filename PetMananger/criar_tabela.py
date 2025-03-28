import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('seu_banco_de_dados.db')

# Criando o cursor para executar comandos SQL
c = conn.cursor()

# Criando a tabela 'animais'
c.execute('''
    CREATE TABLE IF NOT EXISTS animais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especie TEXT NOT NULL,
        raca TEXT,
        idade INTEGER
    )
''')

# Commit e fechamento da conexão
conn.commit()
conn.close()

print("Tabela 'animais' criada com sucesso!")
