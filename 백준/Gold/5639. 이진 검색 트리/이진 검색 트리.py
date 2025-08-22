import sys

def main():
    pre = list(map(int, sys.stdin.buffer.read().split()))
    if not pre:
        return
    n = len(pre)

    val = [0] * n
    L = [-1] * n
    R = [-1] * n


    val[0] = pre[0]
    stack = [0]  

    for k in range(1, n):
        x = pre[k]
        val[k] = x
        last = -1

        while stack and x > val[stack[-1]]:
            last = stack.pop()
        if last != -1:
            R[last] = k
        else:
            parent = stack[-1]
            L[parent] = k
        stack.append(k)

    out = []
    st = [(0, 0)]
    while st:
        u, state = st.pop()
        if u == -1:
            continue
        if state == 0:
            st.append((u, 1))
            if R[u] != -1:
                st.append((R[u], 0))
            if L[u] != -1:
                st.append((L[u], 0))
        else:
            out.append(val[u])

    sys.stdout.write("\n".join(map(str, out)))

if __name__ == "__main__":
    main()
