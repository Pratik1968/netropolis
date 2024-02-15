import sys
from flask import Flask
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="database",
                        host="db",
                        user="username",
                        password="test",
                        port="5432")
@app.route("/")
def hello_world():
    return "<p>pratik won</p>"
@app.route("/api/fetch")
def test():
    cursor = conn.cursor()
    cursor.execute("SELECT  version();")
    app.logger.info("--------------------------")
    test = cursor.fetchone()[0]
    return test
@app.route("/api/test")
def test2():
    return "Test bhai"