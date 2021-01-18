package main

import "fmt"

func main() {
	if 5 > 10 {
		fmt.Println("Es verdadera")
	} else {
		fmt.Println("Es falsa")
	}
	if 10 > 5 {
		fmt.Println("Es verdadera")
	} else if 10 == 10{
		fmt.Println("verdad")
	} else {
		fmt.Println("ninguna")
	}
	fmt.Println("Siempre me voy a ejecutar")

	dia := 2

	switch dia {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	}

}
