
# n=int(input('Ededi daxil edin : '))
# for eded in range(0, n):
#     if eded%2==0:
#         print(eded*0)
#     elif eded%2==1:
#         print(eded*1)


eded1=int(input('Ilk ededi daxil edin :'))
eded2=int(input('Ikinci ededi daxil edin :'))

eded3=eded1+eded2

if eded3 > 0:
    print('Musbet eded')
elif eded3==0:
    print('Toplam 0-a beraberdi')
elif eded3 < 0:
    print('Menfi eded' +'  '+ str(eded3))


