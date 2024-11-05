# FizzBuzz 귀납적으로 생각..

first = input().strip()
second = input().strip()
third = input().strip()

fourth = None

# 어느 하나가 fizz면
# 다음은 integer 아니면 buzz

# 어느 하나가 buzz면
# 다음은 integer 아니면 fizz

# 어느 하나가 FizzBuzz면
# 그 다음 2개는 숫자
# 그 다음이 Fizz

# 15(FizzBuzz) 전까지 반복되는 패턴

if "Fizz" in first:
    if second == "Buzz":
        print("Fizz")
    elif third == "Buzz":
        print("Fizz")
    else:
        fourth = int(third) + 1
        if fourth % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
elif "Fizz" in second:
    if first == "Buzz":
        third = int(third)
        fourth = third + 1
        print(fourth)
    elif third == "Buzz":
        first = int(first)
        fourth = first + 3
        print(fourth)
    else:
        first = int(first)
        fourth = first + 3
        if fourth % 5 == 0:
            print("Buzz")
        else:
            print(fourth)
elif "Fizz" in third:
    if first == "Buzz":
        second = int(second)
        fourth = second + 2
        print(fourth)
    elif second == "Buzz":
        first = int(first)
        fourth = first + 3
        print(fourth)
    else:
        first = int(first)
        fourth = first + 3
        if fourth % 5 == 0:
            print("Buzz")
        else:
            print(fourth)
