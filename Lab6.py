#open file
value = 0
limit = 0
value = int(input("enter value: \n"))
while value < 0:
    value = int(input("enter value: \n:"))
    if value < 0:
        print("error! enter value greater than zero")
    else:
        print("welcome")
if value % 2 == 0:
    print("number is an even number")
else:
    print("number is an odd number")
if is_prime(num):
    print("and it is prime.")
else:
    print("and it is nonprime.")
#
#
