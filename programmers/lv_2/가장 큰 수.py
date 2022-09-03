numbers = [0, 0, 0]

def solution(numbers):

    numbers = sorted(list(map(str, numbers)))[::-1]
    Arr = []

    head = numbers[0][0]
    idx = 0
    container = []
    while idx < len(numbers):
        if head == numbers[idx][0]:
            container.append(numbers[idx])
            idx += 1
        else:
            Arr.append(container)
            head = numbers[idx][0]
            container = []

    Arr.append(container)
    print(Arr)
    def permu(nums, combi):
        if nums == []:
            res.append(combi)
            return

        for idx in range(len(nums)):
            permu(nums[:idx] + nums[idx + 1:], combi + nums[idx])

    ans = ''
    for arr in Arr:
        res = []
        permu(arr, '')
        ans += (max(res))

    return '0' if ans[0] == '0' else ans


print(solution(numbers))


# print(sorted(['1', '3', '2', '20', '873', '89'])[::-1])

print(sorted(['321', '35', '365', '364', '388']))