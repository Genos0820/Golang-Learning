package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello")
}

func main() {
	http.HandleFunc("/", handler)
	log.Println("listening on the port 81")
	err := http.ListenAndServe(":81", nil)
	if err != nil {
		log.Fatal("Server failed to start:", err)
		return
	}
}
