package main

import (
	"fmt"
	"io"
	"os"
)

type logwriter struct{}

func main() {
	fmt.Println(os.Args[1])
	f, err := os.Open(os.Args[1])
	//lw := logwriter{}
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	io.Copy(os.Stdout, f)
}

func (lw logwriter) Write(bs []byte) (int, error) {
	fmt.Println(string(bs))
	return len(bs), nil
}
