#********************{" BOOL TYPE CASTING"}*********************
a=bool(0)
print(a) #False

b=bool(1)
print(b) #True

c=bool(10)
print(c) #True

d=bool(10.5)
print(d)  #True

e=bool(0.178)
print(e) #True

f=bool(0.0)
print(f)#True

g=bool(10-2j)
print(g)#True

h=bool(0+0j)
print(h)  #False

I=bool("True")
print(I) #True

j=bool("False")
print(j) #True

k=bool("") 
print(k) #False
#                    --------(BOOL(x))--------
#     __________________________|________________________________
#     |                |                    |                    |
# {If X is Int }  ! {If X is float }     !{ if X is complex} !{If X is Str }             
#                 !                      !                   !
# (0) means False ! If Total number      ! if both real &    ! If (x) is empty
#                 ! value is zero then   ! imaginary parts   ! String then the
# NON-zero means  ! the result is false  !  are Zero,i.e     ! Result is False
# True.           ! Otherwise the result ! (0+0j) then the   ! Otherwise the 
#                 ! is TRUE.             ! result is False   ! Result is True.
#                 !                      ! Otherwise the     !
#                 !                      ! result is True.   !