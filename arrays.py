# my_array = [4, 8, 10, 9, 3, 7, 6]
# largest_number = max(my_array)
# print("The largest number in the array is:", largest_number)

# my_array = [4, 8, 11, 10, 3, 7, 6]
# largest = my_array[0]
# for num in my_array:
#     if num > largest:
#         largest = num
# print("The largest number in the array is:", largest)

# array1 = [2, 5, 6, 7, 8, 9, 10, 13, 15]
# Use list comprehension to filter out odd numbers and create a new array
# array2 = [num for num in array1 if num % 2 == 1]
# print(array2) # [5, 7, 9, 13, 15]

# array1 = [1, 2, 5, 6, 7, 8, 9, 10, 13, 15]
# array2 = []
# for num in array1:
#     if num % 2 == 1:
#         array2.append(num)
# print(array2)


# set1 = set()
# set1.add(1)
# print(set1)
# print(type(set1))

# dict1 = {}
# dict1["vishnu"]=1
# print(dict1)
# print(type(dict1))

# list1 = []
# list1.append(1)
# print(list1)
# print(type(list1))

# tuple1 =()
# print(type(tuple1))


# list1 = []
# num= int(input("Enter the number:"))
# i=1
# while i<num:
#     if i%2==0:
#         list1.append(i)
#     i+=1
# print(list1)

# dict1 ={
#     "vishnu": 22,
#     "jishnu": 10,
#     "arun": 23
# }
# dict1 ={}
# limit = int(input("Enter the limit: "))
# for i in range(limit):
#     key = input("Enter your key: ")
#     value = int(input("Enter you value:"))
#     dict1[key]=value
# print(dict1)

# Python3 program to find given
# two array are equal or not

# Returns true if arr1[0..n-1] and
# arr2[0..m-1] contain same elements.


# def Equal(arr1, arr2):
# 	if (len(arr1) != len(arr2)):
# 		return False

# 	arr1.sort()
# 	arr2.sort()

# 	for i in range(0, len(arr1)):
# 		if (arr1[i] == arr2[i]):
# 			return True
# 	return False


# arr1 = [3, 5, 2, 5, 2]
# arr2 = [2, 3, 5, 5, 2]
# if(Equal(arr1, arr2)):
#     print("True")
# else:
#     print("false")


# x = str("Hello World")
# x = int(20)
# x = float(20.5)
# x = complex(1j)
# x = list(("apple", "banana", "cherry"))
# x = tuple(("apple", "banana", "cherry"))
# x = range(6)
# x = dict(name="John", age=36)
# x = set(("apple", "banana", "cherry"))
# x = frozenset(("apple", "banana", "cherry"))
# x = bool(5)
# x = bytes(5)
# x = bytearray(5)
# x = memoryview(bytes(5))
# print(type(x))


# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("best" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = " Hello, World! "
# print(a.strip())


# limit = int(input("Enter the limit: "))
# my_list = []
# for i in range(limit):
#     element = input("Enter an element: ")
#     my_list.append(element)

# print(my_list)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = False)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(thislist)
# print(mylist)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)