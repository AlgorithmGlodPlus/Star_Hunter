import sys

input = sys.stdin.readline

N = int(input().rstrip())
strs = [list(input().rstrip().split()) for _ in range(N)]

for str1, str2 in strs:
    asci1 = [0] * 26
    asci2 = [0] * 26
    check = True

    for s in str1:
        asci1[ord(s) - 97] += 1

    for s in str2:
        asci2[ord(s) - 97] += 1

    if asci1 == asci2:
        print("Possible")
    else:
        print("Impossible")