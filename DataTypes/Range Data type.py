#+++++++++++++++++++++"{ Range  data  Type}"+++++++++++++++++++++++

#Range data type represents of numbers.

# the elements presents in range DATA TYPE are not modifies. i.e range Data
#  type is Immutable.

# ******{" FORM-1 "}********:- 
range(10)
r=range(10)
for i in r: print(i) # ---> 0 to 9

# ********{" FORM-2"}*******:-

# generate numbers from 10 to 19
print()
r=range(10,20)
for i in r: print(i) #---> 10 to 19
#10
#11
#12
#13
#14
#15
#16
#17
#18
#19

#************{" FORM-3"}***********:-

range(10,20,2) # 2 means increament values


print()
r=range(10,20,2)
for i in r: print(i) 
#10
#12
#14
#16
#18
