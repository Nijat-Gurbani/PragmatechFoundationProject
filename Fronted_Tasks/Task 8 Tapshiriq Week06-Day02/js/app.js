
let accordionElement=document.querySelectorAll('.panel-body')


function PanelFunction(element){



    for(let i=0; i<accordionElement.length; i++){
        accordionElement[i].className='panel-header passive'

    }


    let nextElement=element.nextElementSibling;
    nextElement.className='panel-header active'


}