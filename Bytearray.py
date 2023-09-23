#***"{BYTE-ARRAY DATA TYPE }"*******


#Bytearray is exactly same as bytes data type except that its elements can be MODIFIED.

x=[10,20,30,40]
b=bytearray(x)
for i in b:print(i)
#10
#20
#30
#40
print()
b[0]=100
for i in b:print(i)
#100
#20
#30
#40

#$$$$$$$$$$$$$$"  NOTE  ":----> ValueError: byte must be in range(0, 256)
                              #|
x=[10,278]                    #|
b=bytearray(x)#---------------#|


