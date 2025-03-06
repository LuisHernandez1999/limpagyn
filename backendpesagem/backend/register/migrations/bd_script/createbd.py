from bd import criar_banco, conectar, desconectar

def criar_tabela_users():
    conn = conectar(dbname="coletaseletiva_pesagem")
    if conn:
        cursor = conn.cursor()
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            print("Tabela 'users' criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a tabela 'users': {e}")
        finally:
            cursor.close()
            desconectar(conn)

def criar_tabela_verificacao():
    conn = conectar(dbname="coletaseletiva_pesagem") 
    if conn:
        cursor = conn.cursor()
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS send_email_reset_password_verificationcode (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,  -- Relacionando com a tabela de usuários
                email VARCHAR(255) NOT NULL,
                code VARCHAR(50) NOT NULL,
                expires_at TIMESTAMP NOT NULL
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            print("Tabela 'send_email_reset_password_verificationcode' criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a tabela: {e}")
        finally:
            cursor.close()
            desconectar(conn)

def criar_tabela():
    conn = conectar(dbname="coletaseletiva_pesagem")  
    if conn:
        cursor = conn.cursor()
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS pesagem (
                id SERIAL PRIMARY KEY,
                peso_calculado FLOAT NOT NULL,
                data TIMESTAMP NOT NULL,
                prefixo VARCHAR(50) NOT NULL,
                motorista VARCHAR(100) NOT NULL,
                cooperativa VARCHAR(100) NOT NULL,
                tipo_veiculo VARCHAR(50) NOT NULL,
                volume_carga FLOAT NOT NULL
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            print("Tabela 'pesagem' criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a tabela: {e}")
        finally:
            cursor.close()
            desconectar(conn)

def criar_tabelas():
    criar_tabela_users() 
    criar_tabela()       
    criar_tabela_verificacao() 

if __name__ == "__main__":
    print("Tentando criar o banco de dados e as tabelas...")
    criar_banco()  
    criar_tabelas()
