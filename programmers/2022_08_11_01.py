# 신고 결과 받기
# Level 1

def solution(id_list, report, k):
    answer = []
    id = {}

    for r in report:
        r = r.split()

        if r[1] not in id:
            id[r[1]] = []
            id[r[1]].append(r[0])
        else:
            if r[0] not in id[r[1]]:
                id[r[1]].append(r[0])

    result = []
    for key in id.keys():
        if len(id[key]) >= k:
            result.append(key)


    r_dict = {}
    for i in id_list:
        r_dict[i] = 0

    for r in result:
        for a in id[r]:
            r_dict[a] += 1

    return list(r_dict.values())