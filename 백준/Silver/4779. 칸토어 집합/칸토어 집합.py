def divide_and_remove(kant, start, end):
    if (end - start) == 1:
        return
    else:
        length = end - start
        checkpoint_1 = start + length // 3
        checkpoint_2 = start + (length // 3) * 2

        for i in range(checkpoint_1, checkpoint_2):
            kant[i] = " "

        divide_and_remove(kant, start, checkpoint_1)
        divide_and_remove(kant, checkpoint_2, end)


import sys


def sol():
    for line in sys.stdin:
        N = int(line.strip())
        kant = ["-"] * (3**N)
        start = 0
        end = len(kant)

        divide_and_remove(kant, start, end)

        result = "".join(kant)
        print(result)


sol()
