# https://www.w3resource.com/python-exercises/python-functions-exercises.php

# 1 

def maxNumber(a, b, c):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    print('Maximum Numer', max)
# maxNumber(8, 12, 5)


# 2
def func():
    sum=0
    list=[8, 2, 3, 0 ,7]
    for element in list:
        sum+=element
    print(sum)
# func()

# 3
def func():
    mul=1
    list=(8, 2, 3, -1, 7)
    for element in list:
        mul*=element
    print(mul)
# func()

# 4

def reverse(str):
   a = ""
   for i in str:
       a=i+a
   return a
str = "1234abcd"
# print('Original string : ', str)
# print('Reserved string : ', reverse(str))

# 5
# Daxil edilen ededin faktorial deyerinin ekrana cap edilmesi
def fact():
    num = int(input('Ededi daxil edin : '))
    f=1
    if num<0:
        print('Menfi ededin fact deyeri olmur')
    else:
        for i in range(1, num):
            f=f*i
        print('Daxil edilen ededin factorial deyeri : ', f)
# fact()

# 6
# Daxil edilen ededin verilen araliqda olub olmamasini yoxlamaq
def check():
    num = int(input('Ededi daxil edin : '))
    if num in range(0, 1000):
        print('Qeyd olunan araliqdadi')
    else:
        print('Qeyd olunan araliqda deyil')
# check()

# 7
def func():
    string='Lorem ipsum dolOr sIt amet, coNsectetur adiPiscing Elit.'

    upper=0
    lower=0

    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print('Upper case letter : ', upper)
    print('Lower case letter : ', lower)
# func()

# 8

def unique():
    list=[2,5,1,5,8,9,10,11,1,2,10,15]
    new_list=[]

    for elm in list:
        if elm not in new_list:
            new_list.append(elm)
    print(new_list)
    
# unique()

# 9

def prime():
    number=int(input('Ededi daxil edin : '))
    if number==1:
        print('1 ne sade ne murekkeb ededdi') 
    elif number%number==1 and number%1==number:
        print('Sade ededdir')
    else:
        print('Sade eded deyil')
# prime()   #bitmeyib

# 10

def even_odd():
    list=[1, 2, 3, 4, 5, 6, 7, 8, 9]

    even_list=[]
    odd_list=[]
    for elm in list:
        if elm%2==0:
           even_list.append(elm)
        elif elm%2==1:
            odd_list.append(elm)

    print('Listdeki cut ededler = ',even_list)
    print('Listdeki tek ededler = ',odd_list)
# even_odd()

# 11
def perfectNumber():
    num = int(input("Yoxlamaq istediyiniz ededi daxil edin: "))
    sum = 0
    
    for i in range(1, num):
        if(num % i == 0):
            sum+=i
    if (sum == num):
        print("Daxil edilen eded mukemmel ededdir : ", num)
    else:
        print("Mukemmel eded deyil : ", num)
        
# perfectNumber()

# 12

def palindrome():

    b=input("Soz daxil edin : ")
    if b==b[::-1]:
        print('It is palindrome')
    else:
        print('It is not palindrome')

# palindrome()








 
