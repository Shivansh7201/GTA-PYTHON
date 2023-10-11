# Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

# Minimum age limit is 
# X (i.e. Age should be greater than or equal to X).
# Age should be strictly less than Y.
# Chef's current Age is A.
# Find whether he is currently eligible to take the exam or not.

 
for _ in range(int(input())): #imput Taken  here
    a=list(map(int,input().split())) #creation of list as well as input Elements
    if a[2] >= a[0] and a[2]< a[1]: # Comparision between list Elements
        print('YES')
    else:
        print('NO')