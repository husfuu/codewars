def solution(number):
    res = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    
    return res


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


res = solution(10)
print(res)