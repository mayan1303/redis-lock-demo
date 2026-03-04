import redis
import uuid

class RedisLock:
    def __init__(self, redis_client):
        self.redis = redis_client

    def acquire_lock(self, lock_name, expire=10):
        identifier = str(uuid.uuid4())

        if self.redis.set(lock_name, identifier, nx=True, ex=expire):
            return identifier
        return None

    def release_lock(self, lock_name, identifier):
        lock_value = self.redis.get(lock_name)

        if lock_value and lock_value.decode() == identifier:
            self.redis.delete(lock_name)
            return True
        return False
