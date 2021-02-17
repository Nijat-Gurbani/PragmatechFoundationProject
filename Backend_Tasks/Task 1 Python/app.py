# Proqrama ad,soyad melumatlari daxil edilir
# Bu melumatlar vasitesi ile Person obyekti yaradilir
# Yaradilan bu obyekt persons adinda bir siyahiya elave edilir
# proqramin idare etme paneli hazirlanir

# Workflow
# 1. Menu hazirlanmasl
# - Yeni istifadeci elave et
# - Id-ye istifadeci melumati gor
# - Butun istifadecileri gor
# - Secilen istifadecini sil
# - Secilen istifadeci melumatlarini deyisdir

# users=[]
users=list()
id=1
class User():
    def __init__(self,_ad,_soyad,_id):
        self.Id=_id
        self.Ad=_ad
        self.Soyad=_soyad
    def showUserData(self):
        print(f"{self.Id} | {self.Ad} | {self.Soyad}")
        return

commandList=[
    "1. Yeni istifadəçi əlavə et ",
    "2. Bütün istifadəçilər",
    "3. Seçilən istifadəçini sil",
    "4. Seçilən istifadəçinin məlumatlarını dəyişdir",
    "5. Əsas menunu göstər"
]
# Console-da 5 daxil edildikdə
def start():
    for item in commandList:
        print(item)

# Console-da 1 daxil edildikdə
def addNewUser():
    global id
    ad=input('Ad: ')
    soyad=input('Soyad: ')
    user=User(ad,soyad,id)
    users.append(user)
    id+=1

# Console-da 2 daxil edildikdə
def showAllUsers():
    for user in users:
        user.showUserData()
# Console-da 3 daxil edildikdə
def deleteUser():
    id=int(input('Silmek istediyiniz istifadecinin id-sini daxil edin : '))
    for user in users:
        if user.Id==id:
            users.remove(user)
# Console-da 4 daxil edildikdə
def updateUser():
    id=int(input('Datani deyisdirmek isdediyiniz istifadecinin id-sini daxil edin : '))
    for user in users:
        if user.ID==id:
            user
            # 
 

start()


while True:
    choise=input('Əmr nömrəsini daxil edin : ')
    print('________________________')
    if choise=='1':
        addNewUser()
    elif choise=='2':
        showAllUsers()
    elif choise=='3':
        deleteUser()
    elif choise=='4':
        updateUser()
    elif choise=='5':
        start()