from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

# Retry logic because MySQL may take a few seconds to be ready
def get_db_connection():
    for _ in range(10):
        try:
            connection = mysql.connector.connect(
                host="mysql",
                user="appuser",
                password="apppassword",
                database="appdb"
            )
            return connection
        except:
            time.sleep(3)
    return None

@app.route("/")
def index():
    conn = get_db_connection()
    if conn:
        return "Python Flask app is running with MySQL using Docker Compose"
    else:
        return "Database connection failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
