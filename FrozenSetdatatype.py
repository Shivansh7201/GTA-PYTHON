# It is exactly same as set except that it is IMMUTABLE.

# Hence we cannot use add or remove FUNCTIONS 

s={10,20,30,40,50}
fs=frozenset(s)
print(fs)
print()
# Command to know the (" TYPE ") 
print(type(fs)) 
print()
print(fs)

print()
for i in fs: print(i)
print()

fs.add(75) 

print()

fs.remove(10)

