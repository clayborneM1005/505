# numbers = int(input('enter number:'))
# for numbers in range(1, numbers):
#     if(numbers % 3 == 0 and numbers % 5 ==0):
#         print(numbers, "Tic Tac")
#     if numbers % 3 == 0:
#         print(numbers, "Tic")
#     if numbers % 5 == 0:
#         print(numbers, "Tac")
#
# # step6
# m = 1
# while m < 16:
#     print(m)
#     m = m + 1
# else:
#     print("finish")
#
# #step 7
# a = int(input("Enter number:"))
# a = 1
# while a < 16:
#     a = a + 1
#     if a % 5 == 0 and a % 3 == 0:
#         print(a, "Tic  Tac")
#     elif (a % 3 == 0):
#         print(a, "Tic")
#     elif a % 5 == 0:
#         print(a, "Tac")

# #step 8
# import random
# print(random.randint(1, 155))

# #step 9
# user_value = 0
# limit = 0
# while user_value >= 0 and limit < 5:
#     user_value = int(input("Enter value: \n"))
#     if user_value <= 0:
#         print("Error! Enter value greater than zero")
#         limit += 1
#     elif user_value >= 0 and user_value <= 10:
#         print("Welcome")
#         break
#     else:
#         print("Invalid")
#         limit += 1
#     if limit == 5:
#         print("Tries exceeded. Account deactivated!")

    #step 10
import random
user_value = 0
limit = 0
user_value = int(input("Enter value: \n"))
main = random.randint(1, user_value)
while user_value > 0 and limit < 6:
        limit += 1
        mynumber = int(input("first guess: \n"))
        if mynumber == main:
            print("perfect")
            break
        elif mynumber != main:
            print("both numbers do not match")
        else:
            print("error")
        if limit == 5:
            print("exit!")
            break





