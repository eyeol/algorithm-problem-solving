import sys

for line in sys.stdin:
    if line.strip() == "0":
        break
    line = line.strip()

    is_palindrome = True

    index_range = int(len(line) // 2)

    for i in range(index_range):
        if line[i] != line[len(line) - 1 - i]:
            is_palindrome = False
            break

    if is_palindrome:
        print("yes")
    else:
        print("no")
