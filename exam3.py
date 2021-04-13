# def func(lis):
#     lis1 = ['Element', 'start', 'finish']
#     lis1.insert(2,lis)
#     return lis1
# print(func(['hello', 5, 'John', ]))
# # ['Element', 'start', 'hello', 5, 'John', 'finish']

def func(**kwargs):
    print(kwargs)

func(x=1, fife=2, John=2)
 # {'x':1, 5:2, 'John':3}
 # # **kwargs
