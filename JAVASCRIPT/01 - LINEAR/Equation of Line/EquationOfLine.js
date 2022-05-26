// A(x1,y1)
const x1 = parseFloat(prompt("x1: "))
const y1 = parseFloat(prompt("y1: "))

// B(x2,y2)
const x2 = parseFloat(prompt("x2: "))
const y2 = parseFloat(prompt("y2: "))


const k = (y1 - y2) / (x1 - x2)

const c = y2 - k  * x2
console.log(`y = ${k}x + ${c}`)

