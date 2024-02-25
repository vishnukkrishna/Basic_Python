# def reverse_string(s):
#     # convert the string to a list of characters
#     chars = list(s)
#     # get the length of the string
#     n = len(chars)
#     # iterate over half of the string and swap its characters
#     for i in range(n // 2):
#         temp = chars[i]
#         chars[i] = chars[n - 1 - i]
#         chars[n - 1 - i] = temp
#     # convert the list of characters back to a string
#     return ''.join(chars)

# s="vishnu"
# result=reverse_string(s)
# print(result)

# string = "vishnu"
# reversed_string = ""
# for i in range(len(string)-1, -1, -1):
#     reversed_string += string[i]
# print(reversed_string)

# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# my_circle = Circle(5)
# area = my_circle.area()
# perimeter = my_circle.perimeter()

# print("Area of circle:", area)
# print("Perimeter of circle:", perimeter)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_count = 0
# even_sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_count += 1

# print("Count of odd numbers:", odd_count)
# print("Sum of even numbers:", even_sum)

# Star printing
# rows = int(input("Enter the number of rows: "))
# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# Largest element in an array
# arr = [5, 2, 8, 10, 4, 3, 1, 6, 7]
# largest = arr[0]

# for i in range(1, len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]

# print("The largest number in the array is:", largest)

# Prime or Not
# def is_prime(number):
#     if number <= 1:
#         return False

#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# print(is_prime(5))

# Multiplication Table
# num = 5
# for i in range(1, 11):
#     print(num, 'x', i,'=',num*i)


# '''Given a fixed-length integer array arr,
# duplicate each occurrence of zero,
# shifting the remaining elements to the right'''

# def duplicate_zeros(arr):
#     length = len(arr)
#     i = 0
#     while i < length:
#         if arr[i] == 0:
#             arr.insert(i+1, 0)
#             arr.pop()
#             i += 2
#         i += 1
#     return arr
# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# result = duplicate_zeros(arr)
# print(result)


# Python Data Types:->
# Numeric - int, float, complex
# String - str
# Sequence - list, tuple, range
# Binary - bytes, bytearray, memoryview
# Mapping - dict
# Boolean - bool
# Set - set, frozenset
# None - NoneType

# dict = {'Name':'Vishnu', 'Age':23, 'Class': 'First'}
# print ("Name:", dict['Name'])
# print ("Age:", dict['Age'])


# def value(arr, key):
#     for i in  range(len(arr)):
#         if arr[i]==key:
#             return i


# list1 = [1,2,3,4,5,6,7]
# valuse_find = 3
# result = value(list1, valuse_find)
# print ("Value:", result)


# result = lambda x,y:x+y

# result1 =result(5,7)
# print(result1)


# list1 = [1,2,3,4]
# list2 = [6,7,8,9]

# table = []

# table = [(x,y) for x in list1 for y in list2]

# for t in table:
#     print(t)


# from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numsLength = len(nums)
#         for i in range(numsLength):
#             for j in range(numsLength):
#                 if i == j:
#                     continue
#                 currSum = nums[i] + nums[j]
#                 if currSum == target:
#                     return [i, j]


# solution = Solution()
# nums = [3, 2, 4]
# target = 6
# result = solution.twoSum(nums, target)
# print(result)

# my_list = [1, 2, 2, 3, 4, 4, 5]

# unique_number = None

# for num in my_list:
#     if my_list.count(num) == 1:
#         unique_number = num
#         break

# if unique_number is not None:
#     print("The unique number is:", unique_number)
# else:
#     print("There are no unique numbers in the list.")


# def linear_recursive(arr, target, index=0):
#     if index >= len(arr):
#         return -1
#     if arr[index] == target:
#         return index
#     return linear_recursive(arr, target, index + 1)


# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# target = 9

# result = linear_recursive(my_list, target)

# if result != -1:
#     print(result)
# else:
#     print("Target not found in the list.")

# def recursive_linear_search(arr, target, index=0):
#     if index >= len(arr):
#         return -1  
#     if arr[index] == target:
#         return index  
#     return recursive_linear_search(arr, target, index + 1)  


# numbers = [4, 7, 2, 1, 9, 3]
# target = 9
# result = recursive_linear_search(numbers, target)

# if result != -1:
#     print(f"Target {target} found at index {result}.")
# else:
#     print(f"Target {target} not found in the array.")


# class Operations():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.a - self.b
#     def mul(self):
#         return self.a * self.b
#     def div(self):
#         return self.a / self.b
    


# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
    
# n1 = Operations(a,b)
# choice = 1
# while choice != 0:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Division")
#     print("4. Multiplication")
    
#     choice = int(input("enter your choice : "))
    
#     if choice == 1:
#         print("Result: ",n1.add())
#     elif choice == 2:
#         print("Result: ",n1.sub())
#     elif choice == 3:
#         print("Result: ",n1.mul())
#     elif choice == 4:
#         print("Result: ",n1.div())

# ..........................................

#  "==" vs "is"

# aa = 'Vishnu'
# bb = 'Vishnu'


# print(aa == bb)  # The print(aa == bb) statement checks for equality between the contents of the variables aa and bb. 
# print()
# print(aa is bb)  # The print(aa is bb) statement checks for identity using the is keyword. It tests whether aa and bb refer to the same object in memory.

# print(id(aa), id(bb))


# ..........................................

# Iterators and Iterables

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)


# self in examples
# class MyClass:
#     def __init__(self, x):
#         self.x = x
    
#     def print_x(self):
#         print(self.x)


# obj = MyClass(10)

# obj.print_x()
