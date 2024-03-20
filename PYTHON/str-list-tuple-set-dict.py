###common
a = [1,2,3,4,8,7,6,1]
b = 'agaghrdasdasd'
c = (1, '2')
d = (1,3)
e = ['a', 'b', 'c']
dd  = {'a': 1, 'b': 2, 'c': 3, 'd':1}
#
# print(a.index(8, 0, 100))
# print(b.index('a', 0, 100))
# print(c.index('2', 0, 100))
# print(c.index(1, 0, 100))




###string
# print(b.split('ga'))
# print(b.partition('ga'))
# print(b.lstrip('agh'))
#
# print('this'.join(e))




###set
# f = {4,1,2,3}
# f2 = {99,999}
# f.update(f2)
# f.add(5)
# try:
#     f.remove(100)
# except Exception as exxp:
#     f.discard(100)
#     print('Error is  = ', exxp)
# f.discard(5)
# print(f)




###list
# print(a[-1:-5:-2])
# print('this'.join(e))
# f = a.copy()
# f.remove(1)
# print(f)
# f.pop(1)
# print(f)




###tuple
# tup = (1,2,3,4,5,1,2)
# print(sorted(tup, reverse=True), tup.count(1))




###dict
# dict  = {'a': 1, 'b': 2, 'c': 3, 'd':1}
# dict2 ={'e': 1, 'f': 2}
# dict3 = dict2.update(dict)
# print(dict.items(), dict.keys(), dict.values())
# print(type(dict.items()), type(dict.keys()), type(dict.values()))
# def get_key_from_value(my_dict, value):
#     return next((key for key, val in dict.items() if val == value), None)
# dict2.pop('e')
# del dict2['f']
# print(dict2)
# print(dict.get('c'))
#
# for key, value in zip(dict.keys(), dict.values()):
#     print(key, '--', value)