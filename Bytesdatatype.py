# <><><><><><><><><" {BYTes DATATYPE} " <><><><><><><><><>

#  ( bytes ) data type represents a group of byte numbers just like an ARRAY!!!

x=[10,20,30,40]
b=bytes(x) 
c=type(b) #<class 'bytes'>
print(c) 
print(b[0]) #--> 10
print(b[-1])#--> 40
print(b[-2]) #--> 30
print()
for i in b: print(i) 
#10
#20
#30
#40

#*********CONCLUSION:-1 -------> The only allowed values for BYTES data type are 0 t0 256.
#                                By mistakes if we are trying o provide any other values then we will get value error!!!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#**********"CONCLUSION:-2"---> Once we create BYTES data type value,we cannot change its values ,Otherwise we will get
#                              "TYPEERROR"

y=[10,20,30,40]
B=bytes(y)
#B[0]=100  --->TypeError: 'bytes' object does not support item assignment  