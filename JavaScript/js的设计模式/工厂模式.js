function Person(name){
    this.name=name
}
Person.prototype.getName=function(){
    console.log(this.name)
}
function Car(model){
    this.model=model
}
Car.prototype.getModel=function(){
    console.log(this.model)
}


function create(type,param){
    return new this[type](param)
}

create.prototype={
    person:Person,
    car:Car
}
var person1=new create("person","zhang san")
person1.getName()
