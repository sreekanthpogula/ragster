import time
import threading

class RateLimiter:
    """
    Thread-safe rate limiter for controlling the number of requests to an API (e.g., LLM API).
    Uses the token bucket algorithm.
    """

    def __init__(self, max_calls: int, period: float):
        """
        :param max_calls: Maximum number of calls allowed in the given period.
        :param period: Time window in seconds.
        """
        self.max_calls = max_calls
        self.period = period
        self.tokens = max_calls
        self.lock = threading.Lock()
        self.last_refill = time.monotonic()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill
        refill_tokens = int(elapsed * (self.max_calls / self.period))
        if refill_tokens > 0:
            self.tokens = min(self.max_calls, self.tokens + refill_tokens)
            self.last_refill = now

    def acquire(self):
        """
        Blocks until a token is available.
        """
        while True:
            with self.lock:
                self._refill()
                if self.tokens > 0:
                    self.tokens -= 1
                    return
            time.sleep(0.01)

# Example usage:
# limiter = RateLimiter(max_calls=5, period=1)  # 5 requests per second
# for _ in range(10):
#     limiter.acquire()
#     call_llm_api()