#********************"TYPE CASTING"*******************

#CONVERTING one type to ANOTHER TYPE --------> {TYPE CASTING}/OR/{TYPE COERSION}

#________________________________________________________________
#***{ Inbuilt Function }***

#1)Int()
#2)float()
#3)complex()
#4)bool
#5)str()

#________________________________________________________________
#    ************" Int() Function "******************

a=int(123.987)
print(a) #FLoat convert to int value

#________________________________________________________________
#>>>***b=int(10+5j)
#>>>***print(b) #TypeError: int() argument must be a string, a bytes-like object or a #real number, not 'complex'

#________________________________________________________________
c=int(True)
print(c)
              #BOOL values converting to int values
d=int(False)
print(d)

#----------------------------------------------------------------

#*************************{ Let's Take Some of the Errors!!!}*************

#>>>>f=int("10.5") 
#>>>>print(f) #ValueError: invalid literal for int() with base 10: '10.5'
#***********************************************************************
#>>>>g=int("ten")
#>>>>print(g) #ValueError: invalid literal for int() with base 10: 'ten'
#**********************************************************************
#>>>h=int("0B1111")
#>>>print(h) #alueError: invalid literal for int() with base 10: '0B1111'

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#**********{RULES & REGULATIONS ABOUT TYPE CASTING}*****************
#
#1)we can convert from any type to { INT} except complex type.
#2)if we want to convert { STRING TYPE } to INT type ,---> It's Compulsory #that """str""" should Contain only integral values and should be secified in #base -0.
#

