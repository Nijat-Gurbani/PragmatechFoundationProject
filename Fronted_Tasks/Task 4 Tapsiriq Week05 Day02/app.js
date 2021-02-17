// 1. contact() metodu

// dovlet ve ozel universitet adlarinin bir array-da (universitet) birlestirilmesi
let dovlet=["BDU","ADU","ADPU"];
let ozel=["Xezer","Odlar Yurdu","Tefekkur"];
let universitet=dovlet.concat(ozel);
console.log(universitet)

// 2. fill() metodu

// array daxilindedki butun deyerleri tek bir static deyer ile deyismek;
let cars=["BMW","MERCEDES","HUNDAI","KIA","TOYOTA"];
cars.fill("Lada")
console.log(cars);

// array daxilindeki verilen index araligindaki deyerleri deyismek;

let cars00=["BMW","MERCEDES","HUNDAI","KIA","TOYOTA"];
cars00.fill("Lada",1,3)
console.log(cars00);

// 3. findIndex() and find()

// Bir massivde verilen emri yerine yetiren "ilk" elementin indexsini gosterir /elementin ozunu gormek ucun find() metodu yerine yetirilir

let students_age=[20,27,18,14,19,13,10]
function check(age){
    return age<=15;
}
console.log(students_age.find(check)) // "15"-den kicik ild element
console.log(students_age.findIndex(check)) // "15"-de kicik ilk elemmentin indeksi

// 4. forEach()

// Massiv daxilindeki butun elementlere eyni funksuyani tetbiq etmek ucun
let array = ['a', 'b', 'c','d','e'];

array.forEach(function(element) {
  console.log(element);
});

// 5. join()

let car=["BMW","MERCEDES","HUNDAI","KIA","TOYOTA"];
console.log(car.join())


// 6. map()

// Massiv daxilindeki elementlere emeliyyat tetbiq edib yeni bir massiv elde ede bilerik

let number=[5,4,1,6,8,2];
console.log(number)
let new_number=number.map(artirma)

function artirma(number) {
    return number + 1;
}
console.log(new_number)

// 7. reverse()

// Maasivi ters cevirir
let mobile=['Iphone','Samsung','Huawei','Xiaomi','Oppo']
console.log(mobile.reverse())

// 8. slice()

//Verilen index araliginda elementlerden yeni massiv(array) yaradir;
let mobile_company=['Iphone','Samsung','Huawei','Xiaomi','Oppo'];
console.log(mobile_company);
let new_mobile_company=mobile_company.slice(2, 4);
console.log(new_mobile_company)

//9.  sort()

//
let b=['Senan','Miri','Zair','Xezer','Aygun'];
console.log(b.sort())

//10. splice()

// Massivde elementlerin silinib elave olunmasi ucun istifade olunur mes:splice(3,4, "elave1","elave2")- burada elave olunacaq indexs 3; elementlerin silinecek indexsi ise elave olunan indexsden hesablanir

let fruits=["Apple","Orange","Fig","Watermelon","Cherry"];
console.log(fruits.splice( 2, 1, "Peach","Mango"));//fruits massivinden silinen elementi gorsedir
console.log(fruits)//elave olunan olunan elementler ile birlikde massivin son veziyyetini gorsedir