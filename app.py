# import math
#
# print("Antonina Vasylieva")
# print('o----')
# print(' ||||')
# print('*' * 10)
# # -----------------------------------------
# price = 10  # int
# rating = 4.9  # float
# name_old = 'Antonina'  # string
# is_published = True  # bool
# print(price)
# print(id(10))
# print(id(price))
# -----------------------------------------
# name = input("What is your name? ")
# color = input("What is your favourite color? ")
# print("Hi, " + name)  # concatenated
# print(name + " likes " + color)
# -----------------------------------------
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)
# -----------------------------------------
# weight_lbs = input("What is your weight (lbs)? ")
# weight_kg = float(weight_lbs) / 2.2
# print(weight_kg)
# -----------------------------------------
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# print(message)
# msg = f'{first} [{last}] is a coder'
# print(msg)
# -----------------------------------------
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)
# print(course.find('P'))  # returns the first position number of symbol
# print(course.find('o'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course)
#
# print(id(course.upper()))
# print(id(course.lower()))
# print(id(course))
#
# print('Python' in course)
# print('python' in course)
# -----------------------------------------
# z = 10 + 3 * 2
# y = 10 + 3 * 2 ** 2
# print(z, y)
#
# x = 2.9
# print(math.ceil(x))
# print(id(x))
# print(id(math.ceil(x)))
# -----------------------------------------
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
# -----------------------------------------
# weight = int(input("Weight: "))
# units = input("(L)bs or (K)g: ")

# if units.upper() == "L":
#   converted = weight * 0.45
#   print(f"You are {converted} kilos")
# elif units.upper() == "K":
#    converted = weight // 0.45
#    print(f"You are {converted} pounds")
# else:
#    print("Please enter again.")
# -----------------------------------------
# secret_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed!")
# -----------------------------------------
# Car Game
# command = ""
# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit the car
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I do not understand.")
# -----------------------------------------
# For Loop
# for item in "Python":
#     print(item)
#
# for item in [1, 2, 3, 4, 4]:
#     print(item)
#
# for item in range(11):
#     print(item)
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
#
# print(f"Total: {total}")
# -----------------------------------------
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
# -----------------------------------------
# numbers = [5, 2, 5, 2, 2]
#
# for item in numbers:
#     print("x" * item)
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)
# -----------------------------------------
# numbers = [1, 4, 6, 2, 1, 0, 8]
#
# biggest = numbers[0]
# for item in numbers:
#     if item > biggest:
#         biggest = item
# print(biggest)
# -----------------------------------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# matrix[0][1] = 20
# print(matrix[0][1])
# -----------------------------------------
# for item in matrix:
#     for num in item:
#         print(num)
# -----------------------------------------
# numbers_new = [4, 6, 4, 2, 4, 1, 0, 8, 4, 4, 4, 6, 6, 8]
# numbers_new.insert(0, 10)
# print(numbers_new)
# numbers_new.remove(10)
# print(numbers_new)
# # numbers_new.clear()
# print(numbers_new)
# numbers_new.pop()
# print(numbers_new)
# print(numbers_new.index(1))
# # print(numbers_new.index(11))
#
# print(11 in numbers_new)
# print(numbers_new.count(4))
# print(numbers_new.sort())
# print(numbers_new)
# numbers_new.reverse()
# print(numbers_new)
# numbers2 = numbers_new.copy()
# numbers_new.append(20)
# print(numbers_new)
# print(numbers2)
#
# print(id(numbers_new))
# print(id(numbers2))
# -----------------------------------------
# numbers = [0, 6, 8, 1, 1, 1, 4, 6, 7, 8, 6]
# uniques = []
# print(numbers)
# for item in numbers:
#     if item not in uniques:
#         # uniques += [item]
#         uniques.append(item)
# print(uniques)
# -----------------------------------------
# numbers = (1, 2, 3)
# # numbers[0] = 10
# print(numbers.index(2))
# -----------------------------------------
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates  # tuple unpacking
# print(x, y, z)
# -----------------------------------------
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["age"])
# print(type(customer))
# -----------------------------------------
# phone = input("Phone: ")
# out = ""
# num_dict = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# print(phone)
#
# for num in phone:
#     out += num_dict.get(num, "!") + " "
# print(out)
# -----------------------------------------
# message = input(">")
# words = message.split(" ")
# print(words)
# emojis = {
#     ":)": "😊",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
# -----------------------------------------
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name} !")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user("John", "Smith")
# greet_user("Mary", "Rosy")
# print("Finish")
# -----------------------------------------
# def square(number):
#     return number * number
#
#
# result = square(3)
# print(result)
# -----------------------------------------
# def square(number):
#     print(number * number)
#     # by default Python return None
#
#
# print(square(3))
# -----------------------------------------
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message_input = input(">")
# print(emoji_converter(message_input))
# -----------------------------------------
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(risk)
#     print(age)
# except ZeroDivisionError:
#     print("Age can not be 0.")
# except ValueError:
#     print("Invalid value")
# -----------------------------------------
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.draw()
# -----------------------------------------
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10, 20)
# point1.x = 30
# print(point1.x)
# -----------------------------------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print("talk")
#         print(f"Hi, I am {self.name}")
#
#
# john: Person = Person("John Smith")
# bob: Person = Person("Bob Smith")
#
# print(type(john))
# print(john.name)
# john.talk()
# bob.talk()
# print(id(john))
# print(id(bob))
# -----------------------------------------
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def mew(self):
#         print("mew")
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
#
# cat1 = Cat()
# cat1.walk()
# cat1.mew()
# -----------------------------------------
# weight = int(input("Weight: "))
# units = input("(L)bs or (K)g: ")
#
# if units.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# elif units.upper() == "K":
#     converted = weight // 0.45
#     print(f"You are {converted} pounds")
# else:
#     print("Please enter again.")
# -----------------------------------------
# import converters
# from converters import kg_to_lbs
#
# print(converters.lbs_to_kg(115))
# print(converters.kg_to_lbs(52))
#
# print(kg_to_lbs(34))
# -----------------------------------------
# import utils
# numbers = [10, 3, 6, 2]
# print(utils.find_max(numbers))
# print(max(numbers))
# -----------------------------------------
# import ecommerce.shipping
#
# ecommerce.shipping.calc_shipping()
# -----------------------------------------
# from ecommerce.shipping import calc_shipping
# calc_shipping()
# -----------------------------------------
import random

# for i in range(3):
#     print(random.random())
#     print(random.randint(10, 20))
# -----------------------------------------
# members = ["John", "Mary", "Bob", "Mosh"]
# leader = random.choice(members)
# print(leader)
# -----------------------------------------
# x = random.randint(1, 6)
# y = random.randint(1, 6)
# print(f"({x}, {y})")
# -----------------------------------------


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice = Dice()
print(dice.roll())
# -----------------------------------------

