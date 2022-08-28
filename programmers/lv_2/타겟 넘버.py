numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):

    answer = 0
    def bi_backtrack(idx, summ):
        #global answer
        nonlocal answer
        if idx == (len(numbers) - 1):
            if (summ + numbers[idx] == target) or (summ - numbers[idx] == target): answer += 1; # since both cannot be met at the same time
            return

        bi_backtrack(idx+1, summ - numbers[idx])
        bi_backtrack(idx+1, summ + numbers[idx])

    bi_backtrack(0, 0)
    return answer

print(solution(numbers, target))