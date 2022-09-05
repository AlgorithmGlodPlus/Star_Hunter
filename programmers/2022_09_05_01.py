# 문자열 압축
# Level 2

def solution(s):
    answer = 1001

    if len(s) == 1:
        answer = 1
    else:
        for i in range(1, len(s)//2 + 1):
            result_word = ""    # 압축된 문자
            cur_word = s[0:i]       # 현재 중복 확인할 문자
            index = 0           # 문자열 인덱스
            count = 0           # 중복 문자 카운트

            while index < len(s) + 1:
                if s[index:index+i] == cur_word:
                    count += 1
                    index += i
                else:
                    if count == 1:
                        result_word += cur_word
                    else:
                        result_word += str(count) + cur_word

                    cur_word = s[index:index+i]
                    count = 0

            result_word += cur_word
            if len(result_word) < answer:
                answer = len(result_word)

    return answer