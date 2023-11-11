# If we Wantt to represent A GROUP of values as KEY-PAIRS then we should go for DICT DATA TYPE.

d={ 101:'shivansh',102:'gupta',102:'is here'}
print(d)
print()
# NOTE :- "DUPLICATE Keys are not allowed but VALUES CAN BE DUPLICATED. If we are TRYING to
#          insert an entry with duplicate key then Old Value will be replaced with new Value.

d[101]='shiva'
print(d)  #{101: 'shiva', 102: 'is here'}
print()
# WE CAN CREATE EMPTY DICTIONARY AS FOLLOWS

d={}

# WE CAN ADD KEY-VALUE PAIRS AS FOLLOWS
d['a']='Shimlamirch'
d['b']='Saboodana'
print()
print(d)

# NOTE :- "dict" is mutable and the order won't be preserved.

#%%%%%%%%%%%%%%%%%%%%%%% NOTE %%%%%%%%%%%%%%%%%%%%%%%%

# 1) In general we can use BYTES and BYTEARRAY data types to represent BINARY information
#    like IMAGES , VEDIO FILES etc,

# 2) IN PYTHON2 long data type is AVIALABLE. BUT in PYTHON3 it is not AVIALABLE and we
#     can represent long values also by using into TYPE ONLY.
# 
# 3) In PYTHON there is no CHAR data type. HENCE we can represent char values also by using  
#     (STR type)    