//  Here is a program to calculate the perimeter 
//  and area of a right-angled triangle 
//  using two legs entered as input



//  prompt() returns a string
let  AB = prompt("Length of the first leg: ")
let AC = prompt("Length of the second leg: ")

//  parseFloat() returns real number if it can be converted
AB = parseFloat(AB)
AC = parseFloat(AC)

//  find the hypotenus 
//  by the pythagorean theorem:
//  "the sum of the squares of the legs
//  is equal to the sqaure of the hypotenuse."
//  The Math.Sqrt() function of the math module
//  returns a squareroot.

const BC = Math.sqrt(AB**2 + AC**2)

//  The area of a triangle is equal to half of the
//  area of the corresponding rectangle
const area = (AB*AC) / 2

//  Perimeter is the sum of all sides.
const perimeter = AB + AC + BC


console.log(`area of the triangle: ${area}`)
console.log(`perimeter of the triangle: ${perimeter}`)