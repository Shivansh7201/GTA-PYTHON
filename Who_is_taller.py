#Alice and Bob were having an argument about which of them is taller than the other.
#Charlie got irritated by the argument, and decided to settle the matter once and for all
#Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X centimeters and Bob's height is Y centimeters. Help Charlie decide who is taller.

#Test case 1: In this case, 150<160 so Bob is taller than Alice.
#Test case 2:   In this case, 160>150 so Alice is taller than Bob.

for _ in range(int(input())):
    A,B=map(int,input().split())
    if A>B:
        print('A')
    else:
        print('B')