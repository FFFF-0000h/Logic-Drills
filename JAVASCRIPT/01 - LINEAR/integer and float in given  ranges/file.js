//  collect upper and lower limit of the range
// Math.random() generates random number from 
alert("enter range for integers:")
const intMin = parseInt(prompt("enter minimum: "))
const intMax = parseInt(prompt("enter Maximum: "))

let n = Math.floor((Math.random() + 0.2) *  (intMax-intMin) + intMin)

console.log("random int:",n)
alert("enter range for floats:")
//  collect upper and lower limit of the range
floatMin = parseFloat(prompt("enter minimum: "))
floatMax = parseFloat(prompt("enter Maximum: "))

n = Math.random() *  (floatMax-floatMin) + floatMin

console.log("random float:",n)

