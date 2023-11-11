#COMPLEX DATATYPE
#		______ (a= real part)
#   a+bj  -----|
#	       |_______(bj=imaginary part)


# REAL PART "SPECIFY" by using {int values}
# but, IMAGINARY PART should be SPECIFIED BY using decimal #form.
#________________________________________
#	a=0b11+5j 
#	print(a)
#	a=3+0b11j
#_______________________________________________
#    a=3+0b11j
#          ^
#SyntaxError: invalid binary literal

#FIXED CODE:-
#____________________________________________
s=10+1.5j
b=20+2.5j
c=s+b
print(c) #print the sum of above two complex data
v=type(c)   # check the type of data
print(v)
#___________________________________________________

#O/p:- (30+4j)
#<class 'complex'>

#___________________________________________________

#CHECKING THE REAL PART AND THE IMAGINARY PART WHILE #(SCIENTIFIC SOLUTION):-

c=10.5+7.6j
c.real
c.imag

