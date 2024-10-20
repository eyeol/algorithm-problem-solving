N = int(input())

words = []
for i in range(N):
    word = input()
    words.append(word)

words = list(set(words))

# lambda 문법 정확하게 공부하기!!
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
