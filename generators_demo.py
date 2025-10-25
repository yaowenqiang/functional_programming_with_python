import time
import requests as rq

def slow_slow_func(st: str) -> str:
    print('Running with:', st)
    time.sleep(1)
    return st[::-1]

names = ['james','matheu', 'charlotte','daniel']
#slow_names_lc = [slow_slow_func(name) for name in names]
fast_names_gc = (slow_slow_func(name) for name in names)
print(next(fast_names_gc))
#print(slow_names_lc)

words = ['cHl0aG9u','aXM=','YXdlc29tZQ==']
base_url = 'https://httpbin.org/base64/{}'
for i in words:
    print(rq.get(base_url.format(i)).text)
