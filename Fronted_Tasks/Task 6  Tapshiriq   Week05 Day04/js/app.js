let imghtml=1

for(let i=0; i<1; i++){
    let section=document.createElement('section')
    section.setAttribute('id', 'section')
    document.body.appendChild(section)



    for(let i=0; i<1; i++){

        let container=document.createElement('div')
        container.setAttribute('class', 'container')
        section.appendChild(container)

        for(let i=0; i<2; i++){
            let row=document.createElement('div')
            row.setAttribute('class', 'row')
            container.appendChild(row)

            for(let i=0;i<3;i++){

                let col=document.createElement('div')
                col.setAttribute('class','col-4')
                row.appendChild(col)
                

                for(let i=0; i<1; i++){
                    let image=document.createElement('img')
                    image.src="../img/" +imghtml+ '.jpg'
                    image.setAttribute('class', 'image')
                    col.appendChild(image)

                        imghtml++
                }  
                
            }
        }
    }
}


