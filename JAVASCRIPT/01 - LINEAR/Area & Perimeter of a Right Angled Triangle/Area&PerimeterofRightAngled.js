/*  Here is a program to calculate the perimeter
 *  and area of a right-angled triangle
 *  using two legs entered as input
*/



//  prompt() returns a string
//  parseFloat() returns real number if it can be converted 
let  AB = parseFloat(prompt("Length of the first leg: "));
let  AC = parseFloat(prompt("Length of the second leg: "));

/*  Find the hypotenuse
 *  by the pythagorean theorem:
 *  "the sum of the squares of the legs
 *  is equal to the sqaure of the hypotenuse."
 *  The Math.Sqrt() function of the math module
 *  returns a square root.
*/

const BC = Math.sqrt(AB**2 + AC**2);

//  The area of a triangle is equal to half of the
//  area of the corresponding rectangle
const area = ((AB*AC) / 2);

//  Perimeter is the sum of all sides
const perimeter = (AB + AC + BC);


console.log(`area of the triangle: ${area}\nperimeter of the triangle: ${perimeter}`);
