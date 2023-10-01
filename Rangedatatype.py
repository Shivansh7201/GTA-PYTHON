#-----> ( RANGE Data type ) represents a sequence of numbers.

#**NOTE**The elements present in the range data type are not modifiable.
#Range datatype are not modifiable.

#%%%%%%%%%%%%%%%%%%%%%% "FORM 1"  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
range(10)                                            #generates 0 to 9 numbers
#--------// OR //
print("FORM 1 O/p")
r1=range(10)                                            #generates 0 to 9 numbers
for i in r1:print(i)


#%%%%%%%%%%%%%%%%%%%%%% FORM 2):-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
r=range(10,20) 
print("FORM 2 O/p")                                        #generates 10 to 19 numbers 
print(r) 
#--------// OR // 
for i in r:print(i)

#$$$$$$$$$$$$$$$$$$$$ FORM 3):-$$$$$$$$$$$$$$$$$$$$$$$$$$$

r=range(10,20,2) #generates 10 to 19 numbers with step size 2
print("FORM 3 O/p")
for i in r:print(i) #10 12 14 16 18

#@@@@@@@@@@ (NOTE) @@@@@@

#  1) We can also acess elments presents in the **RANGE DATA TYPE** by using index.

r=range(10,20)
print(r[0])
#print(r[15]) #IndexError: range object index out of range
print()
print(r[-1]) #19

#  2)  We cannot modify the values of the range data type.
#r[0]=777 #TypeError: 'range' object does not support item assignment

#  3) We can create a LIST OF VALUES with range data type.
print("List crated with range data type")
l=list(range(10,20,2))
print(l) #[10, 12, 14, 16, 18]