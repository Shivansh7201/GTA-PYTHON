#*************{" FUNDAMENTAL DATATYPES "}****************
#                     v/S
#              {   " IMMUTABILITY"   }

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----(1) All fundamental Data types are immutable   @
#        .i.e once we crete an object we cannot     @
#        perform any changes in thet Objects,       @
#        If we are trying to change then with those @
#        changes a new Object will be created.      @
#                                                   @       
#    (*) This Non-changeble behaviour is Called     @
#     ---IMMUTABILITY.                              @
#                                                   @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                                                         8
#---->(2)In PYTHON if a new Objectis requiired ,the PVM wont crete object 8
# immediately .First it will check is any object aviable with the         8
# required with the required content or not.                              8
#                                                                         8
# If avialable then existing object will be reused. it is not avialable   8
# then onlya new object will be created.                                  8  
#                                                                         8
# The advantages of this Approach is memory utilization and performance   8
# will be imporved.                                                       8
#                                                                         8
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

##########################################################################################
#---->(3)                                                                                        %
# But the problem in this appraoch is, several refrences pointing to the same Object, by %
# using one refrence .                                                                   %
#                                                                                        %
# If we are allowed to change the change the content in the existing object then the     %
# remaining refrences will be effected.                                                  %
#                                                                                        %       
# To prevent this Immunatability concept is required.According to this once creats an    %
# an Object we are not allowed to change content, If we are trying to change with those  %
# changes a new object will be created.                                                  %
#                                                                                        %
##########################################################################################

a=45
b=20
print(a is b) #True

#@@@@@@@@@@@@@@@@@@@@@@@@

print(id(a)) #140732202869832

#&&&&&&&&&&&&&&&&&&&&&&&&

print(id(b)) #140732202870152