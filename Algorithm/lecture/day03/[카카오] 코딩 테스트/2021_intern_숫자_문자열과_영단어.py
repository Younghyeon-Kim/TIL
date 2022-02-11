# 카카오 숫자 문자열과 영단어

def solution(s):
    nums = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}
    for k, v in nums.items():
        if k in s:
            s = s.replace(k, v)
        answer = s
    return int(answer)