import math

# Q1
# name = input("Enter your first and last name:\n")
# parts = name.split(" ")
# reversed_name = " ".join(parts[::-1])
# print(reversed_name)


# Q2
# numBase = input("Enter a number:\n")
# num = numBase
# result = 0
# for i in range(0, 3):
#     result += int(num)
#     num += numBase
# print(result)

# Q3
# print(
#     """a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example"""
# )


# Q4
# radius = float(input("Enter the radius of the sphere:\n"))
# def sphereVolume(radius):
#     return (4 / 3) * math.pi * (radius**3)
# print(sphereVolume(radius))


# Q5
# base = input("Enter the base of the triangle:\n")
# height = input("Enter the height of the triangle:\n")
# def triangleArea(base, height):
#     return 0.5 * base * height
# print(triangleArea(float(base), float(height)))


# Q6
# num = int(input("Enter a number:\n"))
# def pyramid(num):
#     for i in range(1, num + 1):
#         print("*" * i)
#     for i in range(num - 1, 0, -1):
#         print("*" * i)
# pyramid(num)


# Q7
# word = input("Enter a word:\n")
# def reverse(word):
#     return word[::-1]
# print(reverse(word))

# Q8
# for i in range(7):
#     if i != 3 and i != 6:
#         print(i)


# Q9
# def fibonacci_series(n):
#     fibonacci_series = []
#     a, b = 0, 1
#     while a < n:
#         fibonacci_series.append(a)
#         a, b = b, a + b
#     return fibonacci_series
# fib_series_up_to_50 = fibonacci_series(50)
# print("Fibonacci series up to 50:", fib_series_up_to_50)
