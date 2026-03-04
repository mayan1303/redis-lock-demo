from flask import Flask
import redis
import time
import os
from redis_lock import RedisLock

app = Flask(__name__)

# Connect to Redis using Railway environment variable
redis_client = redis.from_url(os.environ.get("REDIS_URL"))

lock = RedisLock(redis_client)

@app.route("/")
def home():
    return "Redis Lock Demo Running"

@app.route("/process")
def process():

    lock_id = lock.acquire_lock("my_resource")

    if not lock_id:
        return "Resource is locked by another process"

    print("Lock acquired")

    time.sleep(5)

    lock.release_lock("my_resource", lock_id)

    return "Process completed and lock released"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
