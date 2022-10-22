package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello World")
	for i := 1; i <= 5; i++ {
		for j := i; j > 0; j-- {
			fmt.Print("*")
		}
		fmt.Println()
	}

}
