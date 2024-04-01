###common




###random-functions
##eval
# c,d,e = '[1,2,3,4,5]', '1,2,3', '{1:2,2:3}'
# print(eval(c), type(eval(c)), eval(d), type(eval(d)), eval(e), type(eval(e)))

##zip
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'x': 10, 'y': 20, 'z': 30}
# zipped_keys = zip(dict1.keys(), dict2.keys())
# fff= list(zipped_keys)
# print(type(fff[0]))
# print(fff, type(zipped_keys))
# zipped_values = zip(dict1.values(), dict2.values())
# print(tuple(zipped_values), type(zipped_values))
# result_dict = dict(zip(zipped_keys, zipped_values))
# print(result_dict)
# result_dict = dict(zip(dict1.keys(), dict2.values()))
# print(result_dict)




###os #with
# import os
# if not os.path.exists('testDIRrrr'):
#     os.mkdir('testDIRrrr')
# os.rename('testDIRrrr', 'testDIR')
# print(os.listdir())
# print(os.getcwd())
# os.chdir('/home/niklaus/SWITCH/PYTHON/testDIR')
# print(os.getcwd())
#
# with open('test111.txt', 'w') as f:
#     f.write('HELLOO MOTHFKR !!')
#     f.close()




###print
# import time
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")
#
# print("One", "Two", "Three", sep=", ", end="!")
#
# time.sleep(0.5)
# print("Loading...", end="", flush=True)
# time.sleep(0.5)
# print(" Done!")
#
# numbers = [1, 2, 3, 4, 5]
# print(*numbers)
#
# with open("testDIR/test111.txt", "w") as file:
#     print("YOO HELLOO MOTHFKR !!", file=file)




###function arguments
# NOTE - tuple can be passed, but not dict....below 3 examples are valid
# def xyz(*args):
#     print(type(args))
#     print(args)
# def abc(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# xyz(1,2,3,4,5,'x')
# xyz((1,2,3,'x'))
# abc(a=1,b=2,c="hello")




###datetime #timedelta
# import datetime
#
# start_time = datetime.datetime(2024, 3, 19, 8, 0, 0)
#
# # Creating a datetime object representing the current date and time
# now = datetime.datetime.now()
# print("Current datetime:", now)
#
# # Formatting a datetime object as a string
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_date)
#
# # Parsing a string into a datetime object
# parsed_date = datetime.datetime.strptime("2024-03-19 12:30:00", "%Y-%m-%d %H:%M:%S")
# print("Parsed datetime:", parsed_date)
#
# # Performing arithmetic operations on dates and times
# tomorrow = now + datetime.timedelta(days=1,minutes=3,seconds=23)
# print("Tomorrow:", tomorrow)
#
# # Working with timedeltas
# difference = tomorrow - now
# print("Difference between tomorrow and now:", difference)
# print("Difference between tomorrow and now days:", difference.days)
# print("Difference between tomorrow and now seconds:", difference.seconds)




###fstring #docstring
# pi,x = 3.14159,2
# print(f'Pi is {{}}approximately {pi:.3f}.')
# def double(x):
#     return x * 2
# print(f'The double of {x+pi} is {double(x)}.')
#
#
# def square(x):
#     """
#     Calculate the square of a number.
#     """
#     return x * x
# print(square.__doc__)
# print(__name__)




###map #reduce #filter #list-comprehension
# dict  = {'a': 1, 'b': 2, 'c': 3, 'd':1}
# ll = (key for key, val in dict.items() if val == 1)
# print(ll, type(ll))
# print(next(ll, None))
# print(next(ll, None))
# print(next(ll, None))
# ll = [key for key, val in dict.items() if val == 1]
# print(ll, type(ll))




###generator #next #iter
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# gen = my_generator()
# print(gen)
# print(next(gen))
# print(next(gen))
# for value in gen:
#     print("for loop gen = ", value)
#
# iterr = [1,2,3,4,5]
# # print(next(iterr))
# iterr = iter(iterr)
# print(next(iterr))
# print(next(iterr))
#
# for value in iterr:
#     print("for loop iterr = ", value)




###for #else
# for i in range(5):
#     if i==0:
#         print("ENTERE FOR LOOP")
#         break
# else:
#     print("FOR ELSE")
# for i in []:
#     if i==0:
#         break
# else:
#     print("FOR ELSE WORKED")
