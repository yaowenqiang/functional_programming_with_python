import os
import random as ra

values = [ra.randint(1,100) for _ in range(10)]

float_or_str = [float(i) if i > 50 else str(i) for i in values]
print(float_or_str)


suffixes = ('csv', '.txt')
files = [f"Valid file:{file}" for file in os.listdir() if file.endswith(suffixes)]
print(files)
