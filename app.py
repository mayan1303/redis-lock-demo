from flask import Flask
import threading
import time
import os

app = Flask(__name__)

lock = threading.Lock()

@app.route("/")
def home():
    return "Redis Lock Demo Running"

@app.route("/process")
def process():

    if not lock.acquire(blocking=False):
        return "Resource is locked by another process"

    print("Lock acquired")

    time.sleep(5)

    lock.release()

    return "Process completed and lock released"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
