package main

import "fmt"

type person struct {
	firstName string
	lastName  string
	contactInfo
}

type contactInfo struct {
	email string
	zip   int
}

func main() {
	alex := person{
		firstName: "Alex",
		lastName:  "Anderson",
		contactInfo: contactInfo{
			email: "prawktawri@gmail.com",
			zip:   123,
		},
	}

	alex.updateName("Alexandra")
	alex.details()
	colors := map[string]string{
		"red": "#ff000",
	}
	fmt.Println(colors)
}

func (pointerToPerson *person) updateName(newName string) {
	(*pointerToPerson).firstName = newName
}

func (p person) details() {
	fmt.Printf("%+v", p)
}
