# 시저 암호
# Level 1
def solution(s, n):
    answer = []
    slist = list(s)

    for i in slist:
        asc = ord(i)
        if i == " ":
            answer.append(" ")
        elif asc < 96:
            asc += n
            if asc > 90:
                asc -= 26
            answer.append(chr(asc))
        else:
            asc += n
            if asc > 122:
                asc -= 26
            answer.append(chr(asc))

    return ''.join(answer)