
let  radius = prompt("Radius: ")
radius = parseFloat(radius)


//  length of the circumference is 2*pi*r
const len = 2 * Math.PI * radius

//  The area of the circle is Pi*r*r
const area = Math.PI * Math.pow(radius,2)

//  or 
//  area = Math.PI * radius * radius
//  or
//  area = Math.PI * radius ** 2


console.log("Length: ",len)
console.log("Area: ",area)