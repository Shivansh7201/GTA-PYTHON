#***************{" TYPE CAST THE Complex TYPE"}********
#             _______________|________________
#             |                              |
#         ("FORM -1 ")                   (" form-2")

#        Comlplex(x)                   Complex(x.y)

#>>>> It's convert{x} into complex || >>> We can use this method to convert (x)
#>>>> number with real part and    || >>> and (y) into complex number such that (x)
#>>>>imaginary part (0).           || >>> will be real part and (y) will be IMAGINARY PART.

a=complex(10)
print(a) #(10+0j)

b=complex(True)
print(b)   #(1+0j)

c=complex(False)
print(c)  #0j

d=complex("10")
print(d) #(10+0j)

e=complex("10.5")
print(e)  #(10.5+0j)

# r=complex("ten")
# print(r)  #ValueError: complex() arg is a malformed string

w=complex(10,-2)
print(w)

q=complex(True,False)
print(q)