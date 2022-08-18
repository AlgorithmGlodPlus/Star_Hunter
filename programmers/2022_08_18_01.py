# 모의고사
# Level 1
def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            count[0] += 1

        if answers[i] == second[i % len(second)]:
            count[1] += 1

        if answers[i] == third[i % len(third)]:
            count[2] += 1

    max_count = max(count)
    for i in range(3):
        if max_count == count[i]:
            answer.append(i + 1)

    return sorted(answer)