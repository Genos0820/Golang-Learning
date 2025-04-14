package main

import "fmt"

func main() {
	intList := []int{}
	for i := 1; i <= 10; i++ {
		intList = append(intList, i)
	}
	for _, n := range intList {
		if n%2 == 0 {
			fmt.Println("Even")
		} else {
			fmt.Println("Odd")
		}
	}
}
