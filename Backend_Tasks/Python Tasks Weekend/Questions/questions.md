
#  1. Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin

Interpreted dil - bir programda(codda) emrleri addim addim (setir setir) oruyub masin diline cevirib yerine yetiren dildi. Her hansi setirde problem olsa program o setre qeder isleyir, xeta olan emrden sonraki setrler oxunmur.


#  2. Interpreted və compiler dillər arasında olan fərqləri izah edin

Interpreted və compiler dillər arasında olan fərqlər - 
Interpreted dil - programdaki emrleri addim addim masin diline cevirib icra edir;
            her hansi bir setrde xeta olana qeder emrleri icra edir, bu na gore xetanin aradan qaldirilmasi asant olur.
Compiler dil -  programi butunlukle masin diline cevirir;
            butun programi icra etdikden sonra xeta mesaji verir.

#  3. Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin

    Reqemsal tipler - integer, float, complex
    integer - tam ededler (mes: 42);
    float - kesr ededler (mes: 12.5);
    complex - kompleks ededler (mes: 4d5r).


    Yazi tipi - string
    Yazilisi - tek ve ya cut dirnaq icerisinde yazilan butun deyerler string adlanir. " " ve ya ''' '''.

    Sira(list) tipleri - list, range
    List - [ ] moterizesi icerinde bir birinden ' , ' vergul ile ayrilan deyerler(items) toplumudu.
    List'deki deyerlerin(items) tipleri ferqli ola biler: mes. ['Salam', 5 , 45.2 ]>[string , integer , float]
    
    Range - dongu ucun teyin edilmis mueyyen sayda dongu yaradir. bu sekilde istifade olunur - range(start,stop).



    Boolean tipi - true, false.


    Mapping tipi-dict(dictionary) - siralanmamis maddeler(items) toplusu, her maddede key ve valuse var, { } moterizesi icerisinde yazilir;
        Yazilisi - {
            'name' : 'Nicat',
            'surname' : 'Qurbani'
        }
        - 'name' ve 'surname' key(acar sozler), 'Nicat' ve 'Qurbani' ise key'lere verilmis value(deyerledi).

#  4. Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin
        Real heyatda olan her bir obyekti proqramlasdira bilmekdir.
        
#  5. Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?

Proqramlasdirma hazir metodlardan istifade, codu yazan istifadeci terefinden teyin olunur.



#  6. local və global variable nədir izah edin

local və global variable 
        local deyisken - funksiya daxilinde teyin etdiyimiz deyiskenlere deyilir, bu deyiskenlere teyin olunan funksiya xaricinde istifade etmek mumkun olmur.
            mes: def function():
                    a=20
                    print(a) 
                function()
                print(a)
            yazilmis codda funksiya daxilinde a deyiskeni yaradiriq, codu run etsek funksiya daxilindeki print() funksiyasi bize a deyiskeninin deyerini verecek ancaq funksiya xaricindeki print() funksiyasi ise error verecek('a' is not defined)

        Global deyisken - funksiya xaricinde teyin edilen deyiskenlere deyilir ve bu deyiskenlere istediyimiz yerde cagira bilirik
            mes: a=20
                 def function():
                    print(a)
                 function()
                 print(a)
            yazilmis codda teyin olunmus deyisk=geni ister funksiya daxilindeki ya da ki funksiya xaricindeki print() funksiyasi ile ekrana cap ede bilirik    

#  7. Python type conversion haqqında izahat verin

    Pyhton-da melumat tiplerini deyisdirmek ucun 'Type conversion'-dan istifade olunur. mes: kesr ededin tipini(float) tam eded(int) etmek ucun int(kesr eded) > int(5.4).  

#  8. init nədir?

init-obyekt yaratmaq ucun yaradilan funksiyadir.

#  9. self nedir?

self-Pythonda class'i təmsil edən metodların ilk parametridir, buna gore class daxilindeki metodlari cagirmaq ucun self parametrinden istifade etmeliyik.


#  10. *args,*kwargs nədir? nə zaman istifadə olunur?

    *args - 
    *kwargs - 

#  11. Python module nədir?

Python module(modul) - .py uzantisi olan butun file'lar eslinde bir moduldu. 

#  12. Python package nədir?

Python package(paket) - bir biri ile bagli olan modullara paket deyilir. yeni paketler modullardan yaradilir.

#  13. pass nədir? Nə zaman istifadə olunur?

pass - code daxilinde her hansi funksiyani ve ya emr isletmemek ucun pass beyanatindan istifade edirik.

#  14. List metodlarından 5 ədəd metodun izahatını yazın

list metodlar - 
        append() metodu - liste element elave etmek ucun istifade olunur, listin sonuna elave olunur, yazilisi listname.append();
        sort() metodu - listdeki elementleri mentiqi ardicilliq ile siralayir, yazilisi listname.sort();
        clear() metodu - listdeki butun elementleri silir, yazilisi listname.clear();
        extend() metodu - bir nece listi birlesdirir, yazilisi listname1.extend(listname2);
        insert() metodu - liste element elave etmek ucun istifade olunur, append() metodundan ferqi insert() metodundan istifade etmek ucun elave olunan elementin indeksi bildirilmelidir, yazilisi listname.insert(position, element).

#  15. List və dict hansı hallarda istifadə olunur?

List - bir nece obyekt haqqinda melumati semereli istifade etmek ucun listin icerisine yigib istifade ede bilerik;
Dict - obyekt haqqinda melumati list icinde yiga bilmirikse o zaman dictionary'den istifade edirik.

#  16. Dict metodlarından 5 ədəd metodun izahatını yazın 
        clear() metodu - dict(dictionary) daxilindeki butun elementleri silmek ucun istifade olunur dictName.clear();
        get() metodu - Göstərilən açarın dəyərini qaytarır, yazilisi dictName.get("key")
        keys() metodu - dict daxilindeki keyslerden ibaret list yaradir, yazilisi dictName.keys();
        popitem() metodu - dict son daxil edilmis key-value cütlüyünü silir, yazilisi dictName.popitem()
        update() metodu - yaradilmis key-value cutluyunu dict'e elave edib dict upddate edir, yazilisi dictName.update({"key":"Value"})
