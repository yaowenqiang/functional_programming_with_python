from urllib.parse import urlparse
def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return false

print(is_valid_url('https://www.example.com'))
print(is_valid_url('www.example.com'))
