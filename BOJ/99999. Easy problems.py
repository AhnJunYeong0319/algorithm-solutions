### 15596. 정수 N개의 합 ###

def solve(a: list) -> int:
    return sum(a)

### 1085. 직사각형에서 탈출 ###



def solve(a: list) -> int:
    return min(min(a[0], a[2] - a[0]), min(a[1], a[3] - a[1]))

print(solve(list(map(lambda x:int(x), input().split(' ')   ))))
