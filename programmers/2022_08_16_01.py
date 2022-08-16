# 숫자 문자열과 영단어
# Level 1
def solution(s):
    answer = ""

    ndict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    first = 0
    last = 1
    while last < len(s) + 1:
        #print(s[first:last], answer)
        if s[first:last].isdigit():
            answer += s[first:last]
            first = last
            last = first + 1
        elif s[first:last] in ndict:
            answer += ndict[s[first:last]]
            first = last
            last = first + 1
        else:
            last += 1

    return int(answer)