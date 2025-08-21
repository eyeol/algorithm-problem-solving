import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    result = []
    for _ in range(T):
        N = int(input())

        pre = list(map(int, input().split()))
        ino = list(map(int, input().split()))

        pos = {v: i for i, v in enumerate(ino)}

        post = []
        pre_idx = 0

        def dfs(inL, inR):
            nonlocal pre_idx
            if inL > inR:
                return
            root = pre[pre_idx]
            pre_idx += 1  
            mid = pos[root]

            dfs(inL, mid - 1)
            dfs(mid + 1, inR)
            post.append(root)

        dfs(0, N - 1)
        result.append(" ".join(map(str, post)))

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    solution()
