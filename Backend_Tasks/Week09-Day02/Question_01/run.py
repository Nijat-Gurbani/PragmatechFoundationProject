# https://www.techbeamers.com/python-functions-quiz-part-1/


# q-7

def f(number):
    return number
# print(f(25)) 


# q-8

def func(message, num = 1):
    print(message * num)
 
# func('Welcome')
# func('Viewers', 3)


# q-9

def myfunc(text, num):
    while num > 0:
        print(text)
    num = num - 1
# sonsuz dongu olmasi ucun num > 0 olmalidir
# myfunc('Hello', 4)



# q-11

def func(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)
# func(y = 2, x = 1)



# q-12

num = 1
def func():
    num = 3
    print(num)

# func()
# print(num)



# q-13

num = 1
def func():
    num = num + 3
    print(num)

# func()
# print(num)



# q-19

exp = lambda x: x ** 3
# print(exp(2))


def func(num):
    return lambda eded: eded * num
# number=func(5)
# print(number(15))



# q-20

myList = [
         lambda x: x ** 2,
         lambda x: x ** 3,
         lambda x: x ** 4
         ]
 
for f in myList:
    pass
    # print(f(3))


