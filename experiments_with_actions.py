from typing import List

def only_letters(word:str) -> str:
    return ''.join([char for char in word if char.isalpha()]).title()

text_content = [only_letters(f) for f in open('python_zen.txt').read().split()]
print(text_content)

def encrypt(word: str, shift: int) -> List[int]:
    return [ord(char) + shift for char in word]

def decrypt(encrypted: List[int], shift: int) ->str:
    return ''.join([chr(num - shift) for num in encrypted])

secrect_words = ['python', 'watch', 'process']

encrypted = [encrypt(plantext, 3) for plantext in secrect_words]
print(encrypted)

decrypted = [decrypt(code,3) for code in encrypted]
print(decrypted)
