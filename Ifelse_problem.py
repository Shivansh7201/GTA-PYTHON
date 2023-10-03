#Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

#They consider a turn to be good if the sum of the numbers on their dice is greater than 
# 6
#Given that in a particular turn Chef and Chefina got 
# X and Y on their respective dice, find whether the turn was good.
# cook your dish here
t=int(input())
x,z=map(int,input().split())

for i in range(t):
    if x+z<=6:
        print("YES")
    
    else:
        print("NO")
        
        
