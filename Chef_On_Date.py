# Chef and his girlfriend go on a date. Chef took X dollars with him, and was quite sure that this would be enough to pay the bill.
# At the end, the waiter brought a bill of Y dollars. Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad impression on her.


a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(b>=c):
        print("YES")
    else:
        print("NO")
        
#Test case 1: Since the money Chef has is equal to the bill, he will be able to pay the bill.
#Test case 2: Since the money Chef has is less than the bill, he will have to borrow from his girlfriend and leave a bad impression on her.

