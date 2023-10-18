class point{
    constructor(x,y){
        this.x=x;
        this.y=y
        
    }
      static distance(a,b){
            const x = a.x-b.x;
            const y = a.y-b.y;
        return Math.sqrt(x*x+y*y);
    
    }
}
let p1 = new point(5,5);
let p2 = new point(9,8);
console.log(point.distance(p1,p2));



    