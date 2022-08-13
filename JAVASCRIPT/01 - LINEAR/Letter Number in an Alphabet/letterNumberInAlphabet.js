
const c = prompt("Letter(a-z): ")


const code = c.charCodeAt(0)

// code at "a" = 97 
// being the first letter in the small letter alphabet
// therefore the distance can be gotten by subtracting 
// the code of the first letter from the code of the input letter
// and then the position can be gotten by adding 1
position_ = code - 97 + 1

console.log(`Position of letter ${c} is ${position_}`)
