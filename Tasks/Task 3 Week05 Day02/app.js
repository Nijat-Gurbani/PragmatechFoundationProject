class car{
    constructor(_name, _model, _price){
        this.Name=_name
        this.Model=_model
        this.Price=_price
    }
    showCarDetails(){
        console.log(this.Name+ '/' +this.Model+ '/' +this.Price)
    }
}

let cars=[
    new car('Bmw','X5',25000),
    new car('Audi','',45000),
    new car('Mercedes','4 goz',20000),
    new car('Lada','Niva',10000),
    new car('Naz lifan','Lifan',10000)
]

