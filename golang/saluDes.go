package main

import "fmt"

func main(){
	saludar("Gabriel")
	despedir("Daniela")
}

func saludar(nombre string){
	fmt.Println("hola ",nombre,"como estas")
}
func despedir(nombre string){
	fmt.Println("Chao",nombre,"me voy")
}