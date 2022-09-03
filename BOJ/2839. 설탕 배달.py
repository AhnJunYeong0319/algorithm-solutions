N = int(input())



def counter(N):
    cnt_3 = 0
    while (N - 3 * cnt_3) >= 0 :
        if ((N - 3 * cnt_3) % 5) == 0:
            return cnt_3 + int((N - 3 * cnt_3) // 5)
        else:
            cnt_3 += 1

    return -1

print(counter(N))
