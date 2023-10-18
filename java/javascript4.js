class circle{
    constructor(radius){
        this.radius=radius;
        
    }
    get diameter(){
      return this.radius*2;
    }
    set diameter(value){
          this.radius =  value/2;
         return this.radius;
       
    }
    area(){
        return 3.14*(this.radius*this.radius);

    }
}
let cal = new circle(2)
console.log("Radius: " + cal.radius);
console.log("Diameter : "+ cal.diameter);
console.log("Area: " +cal.area());
cal.diameter = 1.6;
console.log("Radius: " + cal.radius);
console.log("Diameter : "+ cal.diameter);
console.log("Area: " +cal.area());



