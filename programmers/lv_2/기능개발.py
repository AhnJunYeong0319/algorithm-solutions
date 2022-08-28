#progresses = [95, 90, 99, 99, 80, 99]  #-> [5, 10, 1, 1, 20]
progresses = [93, 30, 55]  #-> [7, 70, 45]
#speeds = [1, 1, 1, 1, 1, 1]
speeds = [1, 30, 5]

import math
def solution(progresses, speeds):

    def negs_InaRow(arr):
        for i in range(len(arr)):
            if arr[i] > 0:
                return i
        return len(arr)

    progresses = [(100 - progresses[idx])for idx in range(len(speeds))]
    print(f"progresses : {progresses}")
    res = []
    idx = 0
    while idx < len(progresses):
        n = math.ceil(progresses[idx] / speeds[idx])
        print(f"n : {n}")

        for i in range(idx, len(progresses)):
            progresses[i] -= n * speeds[i]
            print(f"progresses[{i}] : {progresses[i]}")
        cnt = negs_InaRow(progresses[idx:])
        print(f"cnt : {cnt}")

        res.append(cnt)
        idx += cnt

    return res

print(solution(progresses, speeds))