// if (condiciones) {
//    hacemos algo si condicion es true
// } else {
//    hacemos algo si condicion es false
// }

if (5 == 3) {
    console.log("La condicion es verdadera")
} else {
    console.log("La condicion es falsa")
}

console.log("Siempre me voy a ejecutar")
let edad = 29

let mayorDeEdad = edad >= 18 || edad < 20
if (5 > 6) {
    console.log('a')
} else if (8 > 10) {
    console.log('b')
} else if (5 > 3) {
    console.log('c')
} else {
    console.log('d')
}


if (mayorDeEdad) {
    console.log('a')
} else if (mayorDeEdad = 18) {
    console.log('b')
} else if (mayorDeEdad) {
    console.log('c')
} else {
    console.log('d')
}
console.log("Siempre me voy a ejecutar")


// condiconal switch

let dia = "viernes"
switch (dia) {
    case 'lunes':
        console.log("Odio mi vida")
        break
    case 'viernes':
        console.log("Feliz viernes")
        break
    default:
        console.log("No se que dia es hoy")
}