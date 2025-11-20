package main

import "practice/routes"

func main() {
	router := routes.SetupRouter()
	router.Run(":8080")
}
