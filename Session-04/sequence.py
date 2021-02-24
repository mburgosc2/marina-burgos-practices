from pathlib import Path
filename = "../P0/sequences/ADA.txt"
file_contents = Path(filename).read_text()
lines = file_contents.split("\n").replace("\n", "")
count = len(lines(range(1, )))
print(count)