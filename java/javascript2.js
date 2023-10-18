class person{
    constructor(_firstname,_lastname,_age,_email){
        this.firstname=_firstname;
        this.lastname=_lastname;
        this.age=_age;
        this.email=_email;
    }
    toString(){
        return `${this.firstname} ${this.lastname} ${this.age} ${this.email}`}
}
let myPerson = new person('Maria','petterson',22 ,'mp@gmail.com');
let myperson = new person('Lexion',"","","");
let person2 = new person('Stefen','Larsson',25,"");
let person1= new person('Peter','Jansson',24,'ptr@live.com')
console.log(myPerson.toString());
console.log(myperson.toString());
console.log(person2.toString());
console.log(person1.toString());