"""
valrus operator :=
海象运算符
"""
import requests as rq
from urllib.parse import urlparse
print(a := True)
print(F"Value of a: {a}")

def is_valid_string(st: str):
    if len(st) > 3 and st.istitle():
        return [ord(i) for i in st]
    else:
        return False

def return_scheme(st: str) -> str | bool:
    url = urlparse(st)
    if all([url.scheme, url.netloc]):
        return url.scheme
    else:
        return False
items = ["Desk", "ipad", "Hourglass", "tx"]
filtered = [is_valid_string(item) for item in items if is_valid_string(item)]
print(filtered)
filtered = [value for item in items if (value := is_valid_string(item))]
print(filtered)

print(x := len([1,2,3,4]))
print(x)

my_url = 'https://www.baidu.com'
print(code := rq.get(my_url).status_code)
print('And code is now: ...', code)

print(return_scheme('https://www.example.com'))

urls = ['https://www.google.com', 'www.google.com', 'hwww.example.com', 'ftp://localhost']
valid_url = [return_scheme(url) for url in urls if return_scheme(url)]
valid = [scheme for url in urls if (scheme := return_scheme(url))]
print(valid)
