import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    N = int(input())

    depth = [0] * (N + 2)

    size = N + 2
    bit = [0] * size

    def add(i, v=1):
        while i < size:
            bit[i] += v
            i += i & -i

    def psum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def kth(k):
        idx = 0
        bitmask = 1 << (size.bit_length() - 1)
        while bitmask:
            nxt = idx + bitmask
            if nxt < size and bit[nxt] < k:
                idx = nxt
                k -= bit[nxt]
            bitmask >>= 1
        return idx + 1

    root = int(input())
    depth[root] = 0

    cnt = 0           
    out = []
    out.append("0")   

    add(root, 1)
    inserted = 1      

    for _ in range(N - 1):
        x = int(input())

        c = psum(x)

        d_pred = depth[kth(c)]     if c > 0 else -1
        d_succ = depth[kth(c + 1)] if inserted - c > 0 else -1

        depth[x] = max(d_pred, d_succ) + 1

        cnt += depth[x]
        out.append(str(cnt))

        add(x, 1)
        inserted += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solution()
