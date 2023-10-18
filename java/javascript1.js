class rect{
    constructor(_height,_width,_color){
        this.height=_height;
        this.width=_width;
        this.color=_color;
    }
    calsArea(){
        return this.height*this.width;
    }

}
let myRectangle = new rect(4,5,'red');
console.log('Area of Rectangle: ' +myRectangle.calsArea(4,5));
console.log('height:'+ myRectangle.height);
console.log('Width: ' +myRectangle.width);
console.log('Color: ' +myRectangle.color);
