package main

import "fmt"

func main() {
	fmt.Println(suma(4, 5, 7))
	fmt.Println(resta(4, 5, 7))
	fmt.Println(multiplicacion(4, 5, 7))
}

func suma(n, n1, n2 int) int {
	c := n + n1 + n2

	return c
}

func resta(n, n1, n2 int) int {
	c := n - n1 - n2

	return c
}

func multiplicacion(n, n1, n2 int) int {
	c := n * n1 * n2

	return c
}
