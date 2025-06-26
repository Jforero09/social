import oracledb

def get_connection():
    try:
        connection = oracledb.connect(
            user="social",
            password="password123",
            dsn="localhost:1521/XEPDB1"
        )

        if connection:
            print("Conexión exitosa a Oracle")
            return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        print("Error al conectar a Oracle:", error.message)
        return None

get_connection()