let massiv=[1,3,4,90,23,890,12,30,4,3,67,21];

// massivdeki ededlerin(cem) cemi
let cem=0;
    for(i=0; i<massiv.length;i++)
    cem=cem+massiv[i];

console.log(cem)


//massivdeki cut ededlerin(cutcem) cemi
let cutcem=0;
    for(let i=0; i<massiv.length; i++)
    if(massiv[i]%2==0){
        cutcem=cutcem+massiv[i];
    }
 console.log(cutcem)


//massivdeki tek ededlerin(tekcem) cemi
let tekcem=0;
    for(let i=0; i<massiv.length; i++)
    if(massiv[i]%2==1){
        tekcem=tekcem+massiv[i];
    }
console.log(tekcem)

//massivde tekrarlanan ededlerin sayi

//massivde ikireqemli ededlerin sayi
let ikireqemliededler=0;
for(let i=0;i<massiv.length;i++)
    if(String(massiv[i]).length==2){
        ikireqemliededler++
    }

console.log(ikireqemliededler)

//massivde ededlerin azalan sira ile yazilmasi
massiv.sort(function(ededx, ededy,){return ededy-ededx});
console.log(massiv)