from pathlib import Path
filename = "../P0/sequences/RNU6_269P.txt"
file_contents = Path(filename).read_text()
print(file_contents)
