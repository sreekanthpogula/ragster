import functools
import threading
import time


class SimpleCache:
    def __init__(self, max_size=128, ttl=300):
        self.cache = {}
        self.lock = threading.Lock()
        self.max_size = max_size
        self.ttl = ttl

    def _cleanup(self):
        now = time.time()
        keys_to_delete = [k for k, (_, exp) in self.cache.items() if exp < now]
        for k in keys_to_delete:
            del self.cache[k]

    def get(self, key):
        with self.lock:
            self._cleanup()
            if key in self.cache:
                value, exp = self.cache[key]
                if exp >= time.time():
                    return value
                else:
                    del self.cache[key]
            return None

    def set(self, key, value):
        with self.lock:
            self._cleanup()
            if len(self.cache) >= self.max_size:
                # Remove the oldest item
                oldest_key = min(self.cache, key=lambda k: self.cache[k][1])
                del self.cache[oldest_key]
            self.cache[key] = (value, time.time() + self.ttl)

    def clear(self):
        with self.lock:
            self.cache.clear()


def cache(ttl=300, max_size=128):
    cache_instance = SimpleCache(max_size=max_size, ttl=ttl)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            result = cache_instance.get(key)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            cache_instance.set(key, result)
            return result

        return wrapper

    return decorator
