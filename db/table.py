from db.connection import connect_db


def create_table():
    conn = connect_db()
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS transactions (
                     id CHAR(300) PRIMARY KEY NOT NULL,
                     name CHAR NOT NULL,
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                 );
                 """)
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS item (
                     id CHAR(300) PRIMARY KEY NOT NULL,
                     name CHAR(300) NOT NULL,
                     qty INTEGER,
                     price REAL,
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                     transaction_id CHAR(300),
                     FOREIGN KEY(transaction_id) REFERENCES transactions(id)
                 );
                 """)
    conn.close()
