#****************(" Biryani classes Codechef Solution ")*********

#According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make #world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for 
#X weeks, and the cost of classes per week is 
#Y coins. What is the total amount of money that Chef will have to pay?


#Input Format:-

#The first line of input will contain an integer T — the number of test cases. The description of 
#T test cases follows.

#The first and only line of each test case contains two space-separated integers X and Y, as described #in the problem statement.

#** Test case 1:- ** Chef will be required to attend the MasterChef's classes for 11 week and the cost of 
#  classes per week is 10 coins. Hence, Chef will have to pay 10 coins in total.

t = int(input())
for i in range(t):
    X,Y= map(int,input().split())
    m=X*Y
    print(m)