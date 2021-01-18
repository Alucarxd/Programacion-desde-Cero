package main

import "fmt"

func main() {
	var anio int
	fmt.Scanf("Digite el ano %d", &anio)
	if (anio%4 == 0 && anio%100 != 0) || anio%400 == 0 {
		fmt.Println("Ano bisiento")
	} else {
		fmt.Println("Ano NO bisiesto")
	}
}
