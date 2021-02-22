# 10. Listin içindəki ən böyük elementi tapın
def list():

    myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

    newList=[]

    for i in reversed(sorted(myList)):

        newList.append(i)
        
    print(newList[0])

list()