#reversethelist
t=int(input())
while(t>0):
    t=t-1
    l1=list(map(int,input().split()))
    l1.sort()
    l2=list(map(int,input().split()))
    l2.sort()