let project=$('#section-statistic .project, #section-statistic .partner, #section-statistic .member ')
count=1

let dongu=setInterval(function(){
    if(count<=100){
        $(project).html(count)
        count++
    }else{
        clearInterval(dongu)
    }
}, 50)
    
