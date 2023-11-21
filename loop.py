# i = 1
# while i <= 10:
#     print(i)
#     i = i+1
# else:
#     print("Loop Finished")

# for i in range(5):
#     print("Vishnu")

# for i in range(1, 10, 2):
#     print(i)

# sum = 0
# for i in range(1, 11):
#     sum = sum+i
# print(sum)

# num = int(input("Enter a number: "))
# product = 1
# for i in range(1, num+1):
#     product = product*i
# print("Product of the number is ", product)

# Break and Continue
# for i in range(5):
#     num = int(input("Enter the numbers: "))
#     if num == 0:
#         break # continue
#     print(num)

# Prime number
# num = int(input("Enter the number: "))
# for i in range(2, num):
#     if num%i==0:
#         print("Not a prime number")
#         break
# else:
#     print("Prime number")

# def factorial(num):
#     fact=1
#     for i in range(1, num+1):
#         fact=fact*i
#     return fact

# num = int(input("Enter the number: "))
# fact = factorial(num)
# print("Factorial:",fact)

# flag = 10>5
# print(flag,type(flag))

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# for x in range(1,6):
#     print(x)

# for x in range(2, 30, 3):
#     print(x)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# def my_function(name):
#     print(name + " Krishnakumar")

# my_function("Vishnu")
# my_function("Jishnu")
# my_function("Vanaja")

# def my_function(**kid):
#     print("His last name is " + kid["lname"])

# my_function(fname = "Vishnu", lname = "Krishnakumar")

# Default Parameter Value
# def my_function(country = "Norway"):
#     print("I am from " + country)

# # my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# x = lambda a : a + 10
# print(x(5))

