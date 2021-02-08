let slider = [
    {

        name:'Adventurer Lemon',
        image:'./img/1.jpg'

    },
    {

        name:'Adventurer Donut',
        image:'./img/2.jpg'

    },
    {

        name:'Adventurer Caramel',
        image:'./img/3.jpg'

    },
    {

        name:'Adventurer Cheesecake Brownie',
        image:'./img/4.jpg'

    }

    
];

let index=0;

showSlide(index);

document.querySelector('.fa-arrow-circle-left').addEventListener('click',function(){
index--;
showSlide(index);
console.log(index);

});

document.querySelector('.fa-arrow-circle-right').addEventListener('click',function(){
    index++;
    showSlide(index);
    console.log(index);
      
});

function showSlide(i){
    
   index=i;

    if(i<0){
        index=slider.length - 1;
    }

    if(i>=slider.length){
        index =0;
    }
    document.querySelector('.img-name').textContent = slider[index].name;

    document.querySelector('.img').setAttribute('src', slider[index].image)
}

