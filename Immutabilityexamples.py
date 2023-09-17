#---------------{"Immutability Examples"}---------------
a=19
b=56
print(id(a)) #140732202870120
print(id(b)) #140732202871304
print(a is b) #False
print()
#---------------------------------------------------------
a=10+5j
b=10+6j
print(a+b) #(20+11j)
print(id(a)) #2272478280880
print(id(b)) #2272478280976
print()

#-----------------------------------------------

a=True 
b=False
print(a is b) #False
print(id(a))  #140732201343848
print(id(b))  #140732201343880
print()
#---------------------------------------------------------

a='durga'
b='soft'
print(a is b) #False
print(id(a))  #1682263276272
print(id(b))  #1682263276144