#*************************{" Set Data Type "}******************

# NOTE :- If we want to represent a group of values without duplicates where order is not important,
#         then we should go for SET DATA TYPE.

#--->  || 1) Insertion order is not preserved. ||
#--->  || 2) Duplicates are not allowed.  ||
#--->  || 3) Indexing and slicing are not applicable  ||
#--->  || 4) Heterogeneous objects are allowed.  ||
#--->  || 5) Growable in nature.   ||

s={100,0,10,200,101,'durga'}
print(s) # {0, 100, 101, 'durga', 10, 200}
print()
print(type(s)) # <class 'set'>
print()
#print(s[0]) # TypeError: 'set' object does not support indexing

# %%%%%%%%%% NOTE "SET is growable in nature, based on our requirement we can increase OR " %%%%%%%%%%%%%
# %%%%%%%%%% "decrease the size. There is no restriction. " %%%%%%%%%%%%%

s.add(742)
print(s) # {0, 100, 101, 'durga', 10, 200, 742}
print()
s.remove(200)
print(s) # {0, 100, 101, 'durga', 10, 742}