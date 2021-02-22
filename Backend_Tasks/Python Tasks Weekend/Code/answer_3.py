# 3. Listin içində cüt yerdə duran elementləri ekrana çap edin

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

newList=[]

def list():
    for elm in range(0, len(myList)):
        if elm%2==0:
            newList.append(myList[elm])
    print(newList)
list()