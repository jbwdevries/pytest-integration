import time

def short_method(in_put: str) -> str:
    return in_put[::-1]

def medium_method(in_put: str) -> str:
    time.sleep(0.1)
    return in_put[::-1]

def long_method(in_put: str) -> str:
    time.sleep(1)
    return in_put[::-1]
