### Recursive approacch (similar to the number of islands problem in LeetCode) ###

n = 1
computers = [[1]]

def solution(n, computers):
    def dfs(curNode, visited): ## dfs definition

        visited[curNode] = 'o'
        for node in graph[curNode]:

            if visited[node] != 'o':
                dfs(node, visited)

    ## computers -> graph form changed ##
    graph = []
    for ith in range(n):

        container = []
        for jth in range(n):

            if (computers[ith][jth] == 1) and (ith != jth):
                container.append(jth)

        graph.append(container)
    ## computers -> graph form changed ##


    visited = ['x' for i in range(n)]
    res = 0

    for i in range(n):
        if visited[i] != 'o':
            dfs(i, visited)
            res += 1

    return res

print(solution(n, computers))



### Iterative approacch ###

n = 1
computers = [[1]]


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):

        stack = [start]
        while stack:

            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1

            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)


    i = 0

    while 0 in visited: # early stopping when all the computers are checked
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer
print(solution(n, computers))