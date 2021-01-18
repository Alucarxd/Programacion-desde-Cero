let anio = Number(promt('Digite el ano'))

if ((anio % 4 === 0 && anio % 100 != 0) || anio % 400 === 0) {
        console.log("Ano bisiento")
    } else {
        console.log("Ano NO bisiesto")
    }