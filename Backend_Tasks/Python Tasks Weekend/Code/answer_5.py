#5. Listin içində təkrarlanan elementləri tapın

def list():
    myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

    newlist=[]

    for elm in myList:
        if myList.count(elm)!=1:
            newlist.append(elm)
    print(newlist)

list()

  
    