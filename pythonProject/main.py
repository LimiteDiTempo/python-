def DFS(v, a, s, visited):
    visited[s] = True

    for i in range(len(v)):
        if a[s][i] != 0:
            if visited[i] == False:
                DFS(v, a, i, visited)


a, b, c = map(int(input().split(',')))
