# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# sum = num1 + num2
# print("Sum:", sum)

# rad = int(input("Enter the radius: "))
# area = 3.14*rad**2
# print("Area is ",area)

# s = "Hi Everyone"
# print(s.upper())
# print(s.lower())
# print(s.find("v"))

# Indexing and Slicing
# s= "Hello World"
# for i in range(len(s)):
#     print(s[i])
# print(s[4])

# s= "HelloWorld"
# print(s[1:len(s):2])
# v= "Vishnu"
# print(v[::-1])

# List
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10,list1]
# print(list1)
# print(list2)

# fruit = ["apple","orange","banana","grapes"]
# print(fruit[3])
# print(fruit[1:4:2])

# append(), insert()
# list1 = [1,2,3,4]
# item=int(input("Enter your element: "))
# list1.append(item)
# list1.insert(2,item)
# print(list1)

# extend()
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list1.extend(list2)
# print(list1)

# pop()
# list1 = [1,2,3,4]
# removed = list1.pop(1)
# print(list1)
# print(removed)


# Set memebership# Set memebership
# num_set = {1,2,3,4,5}
# print(1 in num_set)
# print(5 in num_set)


# my_set = {1, 2, 3, 4, 5}
# my_tuple = tuple(my_set)
# print(my_tuple)
# my_tuple = tuple(my_set)
# print(my_tuple)

# student = {
#     'Name': 'vishnu',
#     'Age': 23,
#     'Marks': [10,20,30,40]
# }
# print(student)

# student.update({
#     "Department": 'CSE'
# })
# print(student)
# student.pop("Name")
# print(student)
# student = {
#     'Name': 'vishnu',
#     'Age': 23,
#     'Marks': [10,20,30,40]
# }

# student.update({
#     "Department": 'CSE'
# })
# print(student)
# student.pop("Name")
# print(student)
# student.popitem()
# print(student)
# student.popitem()
# print(student)

# Lambda Function
# one = lambda x:x+1
# print(one(6))
# two = lambda x,y:x*y
# print(two(4,6))

# Map fuction
# def cube(num):
#     return num**3
# print(list(map(cube, [1,2,3,4])))

# num = [1,2,-3,4,-5]
# print(list(map(lambda x:x+1, num)))