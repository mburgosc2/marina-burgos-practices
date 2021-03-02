from pathlib import Path
filename = "../P0/sequences/RNU6_269P.txt"
file_content = Path(filename).read_text()
lines = file_content.split("\n")
print(lines[0])