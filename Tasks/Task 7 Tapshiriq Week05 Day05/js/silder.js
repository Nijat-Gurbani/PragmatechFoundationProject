let images=['img/1.jpg','img/2.jpg','img/3.jpg','img/4.jpg']
let bashliq=['Adventurer Lemon','Adventurer Donut','Adventurer Caramel','Adventurer Cheesecake Brownie']
let ul=''

for(let i=0; i<images.length; i++){
          let li=`


        <li class="li">
            <img src=${images[i]} alt="">
        </li>
    
    `
    ul+=li

    

    
    

  
    
    
}
document.querySelector('.imgs').innerHTML=ul

