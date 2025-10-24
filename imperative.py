import os

files = []

for file in os.listdir():
    if file.endswith('.txt'):
        files.append(file)

file_content = []

for txt_file in files:
    with open(txt_file) as file:
        file_content.append(file.read())
        
        
