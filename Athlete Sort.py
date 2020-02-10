def sortKey(val,position):
    return val[position]

NandM = input().split()
N=NandM[0]
M=NandM[1]

Athletes=[None]*int(N)
for i in range(int(N)):
    Athletes[i]=list(map(int,input().split()))
k=int(input())
Athletes.sort(key=lambda Athletes: Athletes[k])
for i in range(int(N)):
    print(" ".join(list(map(str,Athletes[i]))))
