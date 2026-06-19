import glob
import sys

for file in glob.glob("*.py"):
    with open(file) as f:
        lines = len(f.readlines())

    if lines > 100:
        print(f"{file} exceeds 100 lines")
        sys.exit(1)

print("All files are within 100 lines")
