//  Step1: Understand the problem (research and comprehension)



//  get cylinder height
const h = parseFloat(prompt("enter height: "))

//  cylinder base radius 
r = parseFloat(prompt("enter radius: "))

//  As a cylinder as two bases
//  and the area of each is (pi*r**2)

const bases = 2 * Math.PI * r**2

//  The area of the side surface of cylinder = 2*pi*r* h

const sides = 2 * Math.PI * r * h

//  total surface area 
const area = sides + bases

console.log("Area: ",area)