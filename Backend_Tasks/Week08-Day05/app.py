
# # Task 1

a=int(input('Ilk reqemi daxil edin : '))
b=int(input('Ikinci reqemi daxil edin : '))

print((a+b)/2)

#Task 2

def istifadeci():
    username=input('Username daxil edin : ')
    password=input('Password daxil edin : ')

    if username=='admin' and password=='123456':
        print('Valid')
    else: 
        print('Invalid')

istifadeci()

#Task 3




#Task 4

def soz_sayi():

    meqale="Baş nazir bildirib ki, müxtəlif sahələrdə əməkdaşlığımızı nəzərdə tutan bir çox sənədlər dünən keçirilən görüşlərdə imzalanıb: “Bu, çoxtərəfli platforma gələcək üçün böyük perspektivlər vəd edir. Əminəm ki, bu gün keçirilən iclasın nəticələri ikitərəfli münasibətlərin inkişafına da təkan verəcək. Prezident İlham Əliyev və Rəcəb Tayyib Ərdoğanın yorulmaz səyləri nəticəsində ölkələrimiz arasında münasibətlər ən yüksək səviyyəyə çatıb. Əməkdaşlığımız bütün sahələri əhatə edir. 2023-cü ilədək ticarət dövriyyəmizi 15 milyard dollara çatdırmaq əsas hədəflərimizdəndir”."
    print(len(meqale.split()))
    
soz_sayi()