#  *****************"{LIST DATA TYPE}"*********************

#--> If we want to represent a group of values as a SINGLE ENTITY where
#    INSERTION Order required to preserve and DUPLICATE are allowed then we should go for list 
#     DATATYPE.

#1) Insertion Order is Preserved.

#2)HETEROGENOUS Obejects are allowed.

#3) Duplicate are allowed.

#4) GROWABLE in Nature.

#5) Values should be enclosed within Square Brackets.

list=[10,20,30,40,50]
print(list[0])   
print(list[-1])
print(list[1:3])
print(list[:])
print(list[:2])
print(list[:4])
print(list[2:])
print(list[0:0])                   

#OUTPUT:-    10
            #50
            #[20, 30]
            #[10, 20, 30, 40, 50]
            #[10, 20]
            #[10, 20, 30, 40]
            #[30, 40, 50]
            #[]
print()
list[1]=108
for i in list: print(i)

#Output:-

#10
#108
#30
#40
#50

list=[10,10.5,'durga',True,10]
print(list) #[10, 10.5, 'durga', True, 10]

# LIST ---> It's growable in Nature i.e based on our requirement we can increase /or/
#           decrease the SIZE.

list=[10,20,30,40,50]
list.append("durga")
print(list)
print()
list.remove(20)
print(list)
list2=list*2
print(list2)

#*********" NOTE "----> An Ordered , mutable, heterogenous collection of elements is nothing 
#                        list , WHERE DUPLICATE ALSO ALLOWED.