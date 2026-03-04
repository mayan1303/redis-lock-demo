from flask import Flask
import redis
from redis_lock import RedisLock
import time

app = Flask(__name__)

redis_client = redis.Redis(host='localhost', port=6379, db=0)
lock = RedisLock(redis_client)

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
    app.run(debug=True)
