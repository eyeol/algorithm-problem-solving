notes = list(map(int, input().split()))

ascend_notes = sorted(notes)

descend_notes = sorted(notes, reverse=True)

if notes == ascend_notes:
    print("ascending")
elif notes == descend_notes:
    print("descending")
else:
    print("mixed")
