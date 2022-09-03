numbers = [232, 23]

def solution(numbers):
    if max(numbers) == 0:
        return "0"
    numbers = list(map(lambda x:str(x)*3,numbers))
    numbers.sort(reverse=True)

    return ''.join(map(lambda x:x[:len(x)//3],numbers))


print(solution(numbers))


# print(sorted(['1', '3', '2', '20', '873', '89'])[::-1])

#print(sorted(['321', '35', '365', '364', '388']))