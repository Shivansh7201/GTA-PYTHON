#****************" { TUPLE DATA TYPE } "*******************

#Tuple data type is exactly same as list data type EXACT that it is immutable i.e 
# we cannot change values.


#Tuple elements can be represents within PARENTHESIS.

t=(10,20,30,40,50,60)
print(type(t)) #<class 'tuple'>

# t[0]=100 ---->  TypeError: 'tuple' object does not support item assignment 

# t.append(10)----->  AttributeError: 'tuple' object has no attribute 'append'

#  t.remove(10)----> AttributeError: 'tuple' object has no attribute 'remove'

#-------> Tuple is the read only version of list
