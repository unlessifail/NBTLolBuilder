import sqlite3

# Conectar ao banco de dados (um arquivo será criado se não existir)
banco = sqlite3.connect('usuarios.db')

# Criar um cursor para executar comandos SQL
cursor = banco.cursor()

# Criar uma tabela para armazenar os dados dos usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        agentID TEXT PRIMARY KEY,
        agentName TEXT,
        agentShift TEXT,
        agentManagerName TEXT,
        regionID INTEGER,
        regionEND TEXT,
        timeOnFunc TEXT
    )
''')

   # dados_agente = [agentID, , regionID, agentShift, agentName, agentManagerName, regionEND]

# Inserir dados na tabela
#cursor.executemany('INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?)', usuarios_exemplo)

# Commit para salvar as alterações
#banco.commit()
