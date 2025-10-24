import os
file_content = [open(file).read for file in os.listdir() if file.endswith('.txt')]
