from pathlib import Path
current_dir = Path.cwd()
directories = [d.name for d in current_dir.iterdir() if d.is_dir()]
print(directories)
