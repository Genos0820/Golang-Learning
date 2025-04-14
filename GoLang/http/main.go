package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

type logWriter struct{}

func main() {
	res, err := http.Get("https://google.com")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	// bs := make([]byte, 99999)
	// n, e := res.Body.Read(bs)
	// fmt.Println("Response: ", string(bs), n, e)
	// io.Copy(os.Stdout, res.Body)
	lw := logWriter{}
	io.Copy(lw, res.Body)
}

func (logWriter) Write(bs []byte) (int, error) {
	fmt.Println(string(bs))
	return len(bs), nil
}
