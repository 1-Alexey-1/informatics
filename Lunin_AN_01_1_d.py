n=int(input('введите число '))
dx,dy=1,0
x,y=0,0
sp=[[None]*n for c in range(n)]
for i in range(1,n**2+1):
    sp[x][y]=i
    nx,ny=x+dx,y+dy
    if 0<=nx<n and 0<=ny<n and not sp[nx][ny]:
        x,y=nx,ny
    else:
        dx,dy=-dy,dx
        x,y=x+dx,y+dy
for j in range(len(sp)):
    for v in range(len(sp)):
        print(sp[v][j], end=' ')
    print()