#%%%%%%%%%%%%%%%%%%%%%{ " TYPECASTING OF FLOAT() VALUES"}%%%%%%%%%%%%
#
#  Float() use to convert other values to Float values.

a=float(100)
print(a) #100.0

#b=float(10+5j)
#print(b)------->TypeError: float() argument must be a string or a real number, not 'complex'
#

c=float(True)
print(c) #1.0

d=float(False)
print(d) #0.0

v=float("10")
print(v) #10.0

##################{ "NOW CHECK SOME ERROR's"}################

#>>>>s=float("ten")
#>>>>print(s) #ValueError: could not convert string to float: 'ten'

#>>>>e=float("0B111")
#>>>print(e) #ValueError: could not convert string to float: '0B111'

#************************[ ------" IMPOTANT POINTS REGARDING "]************

#we can covert any type of value to float type except COMPLEX TYPE.
#Whenever we are trying to converting "STR" type value to Float type value,
# it's compulsory "str" should be either integral point literal & should be specified only in base -10.