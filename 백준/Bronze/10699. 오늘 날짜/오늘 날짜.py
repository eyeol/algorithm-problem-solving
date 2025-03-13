import sys
import datetime

input = sys.stdin.readline  # 빠른 입력


def solution():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(today)


solution()
