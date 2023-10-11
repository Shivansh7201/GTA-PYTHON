#On a sunny Sunday afternoon, Chef prepared a brunch for his 20 neighbours.
#Chef prepared a total of X plates. However, the meal was so good that the neighbours started taking Y plates each.
#Find the maximum number of neighbours Chef can feed completely.

#Test case 1: Chef prepared 20 plates and each neighbour eats 1 plate. Thus, Chef can feed all 20 neighbours.

#Test case 2: Chef prepared 100 plates and each neighbour eats 4 plate. Thus, Chef can feed all 20 neighbours and still have 20 plates left.

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if(x//y>=20):
        print(20)
    else:
        print(x//y)
