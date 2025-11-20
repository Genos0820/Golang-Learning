package main

import "fmt"

func main() {
	char := []string{"a", "a", "b", "b", "c", "d"}
	seen := make(map[string]int)
	for i, c := range char {
		if _, exists := seen[c]; exists {
			seen[c]++
			fmt.Print(c, seen[c])
		} else {
			seen[c] = 1
			fmt.Print(c, seen[c])
		}
		if i != len(char)-1 {
			fmt.Print(",")
		}
	}
}
