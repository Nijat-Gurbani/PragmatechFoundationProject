# people=['Hecibala', 'Memmed', 'Sabir', 'Tamerlan', 'Jale', 'Fatime']

elm=[3,56,78,12,56,25]
def filterNumbers(expression):
    for eded in elm:
        if expression(eded):
            print(eded)
# filterNumbers(lambda x:x%5==0)
# filterNumbers(lambda x: x<10)


isciler=[
    {
        'ad':'Memmed',
        'maas':'600AZN'
    },
    {
        'ad':'Cemile',
        'maas':'500AZN'
    },
    {
        'ad':'Saleh',
        'maas':'1200AZN'
    },
    {
        'ad':'Gulnar',
        'maas':'980AZN'
    }
]

def maas():  
    isciMaas=[]
    for maasi in isciler:
        isciMaas.append(maas["maas"])
    return maasi
print(maas())

def gross(maasi):
    gross_maas=[]
    for reqem in maasi:
        maaslar = reqem[:-3]
        gross_maas.append(maaslar)
    return gross_maas

# print(gross())


    # for i in isciler:
    #     maaslar=list(map(lambda i: i , isciler(i["maas"])))
    # print(maaslar)

    # for i in isciler:
    #     maaslar.append(i["maas"])
    # return maaslar
# Sum()      
# maaslar= Sum()
# print(maaslar)


# maas=['600AZN','1200AZN','500AZN']
# maas2=[]
# for elm in maas:
#     maasElm=elm[:-3]
#     maas2.append(maasElm)
# cem=0
# for i in maas2:
#     cem+=i
# # print(cem)

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(map(lambda x: x*0.82 , my_list))

# print(new_list)