import sys
read = sys.stdin.readline
n, m, v = map(int, read().split())
graph, visit_list, visit_list2 = [[0] * (n + 1) for _ in range(n + 1)], [0] * (n + 1), [0] * (n + 1)
for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1
def dfs(v):
  visit_list2[v] = 1
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1: dfs(i)
def bfs(v):
  q, visit_list[v] = [v], 1
  while q:
    v = q.pop(0)
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1: q.append(i); visit_list[i] = 1

dfs(v)
print()
bfs(v)
