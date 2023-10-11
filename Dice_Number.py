#Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
#The score of a player is the maximum number that can be formed using the rolls.
#The player with the highest score wins, and the game ends in a tie if both players have the same score.
#Find the winner of the game or determine whether it is a tie.

#(TEST CASE 1)Alice's score is 532 which is less than Bob's score 611
#(TEST CASE 2) Alice's score is 544 which is same as Bob's score 544.

# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a=l[:len(l)//2]
    b=l[len(l)//2:]
    a.sort(reverse=True)
    b.sort(reverse=True)
    if(a>b):
        print("Alice")
    elif(a<b):
        print("Bob")
    else:
        print("Tie")


