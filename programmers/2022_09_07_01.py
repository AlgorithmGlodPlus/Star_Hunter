# 오픈채팅방
# Level 2

def solution(record):
    answer = []
    acs = []
    id = {}

    for r in record:
        s = r.split()
        acs.append([s[0], s[1]])
        if s[0] == 'Enter' or s[0] == 'Change':
            id[s[1]] = s[2]

    for a in acs:
        if a[0] == 'Enter':
            answer.append(id[a[1]] + '님이 들어왔습니다.')
        elif a[0] == 'Leave':
            answer.append(id[a[1]] + '님이 나갔습니다.')

    return answer