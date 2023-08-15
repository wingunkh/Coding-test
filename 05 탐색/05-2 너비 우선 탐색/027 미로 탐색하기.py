from collections import deque

def BFS(row, col):
    q = deque()
    q.append((row, col))
    
    while q:
        row, col = q.popleft()
        
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1:
                    a[nr][nc] = a[row][col] + 1
                    q.append((nr, nc))
            
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]

BFS(0, 0)
      
print(a[n-1][m-1])
