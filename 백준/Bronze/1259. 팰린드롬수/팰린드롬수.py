import sys

for line in sys.stdin:
    if line.strip() == "0":
        break
    line = line.strip()

    if line != line[::-1]:
        print("no")
    else:
        print("yes")
