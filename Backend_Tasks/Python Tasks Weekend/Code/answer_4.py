#4. Listin elementlərini azalan sıra ilə sıralayaraq ekrana çap edin

def list():
    myList=[1,34,56,100,-12,87,987,1,3,5,56,67]
    for i in reversed(sorted(myList)):
        print(i)
list()