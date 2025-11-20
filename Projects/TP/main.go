package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	runtime.GOMAXPROCS(1) // Limit to 1 CPU core to potentially make the race more apparent
	var counter int
	var wg sync.WaitGroup
	oddChan := make(chan int)
	nummap := make(map[string]string)
	age := map[string]int{
		"Alice": 30,
	}
	age["bob"] = 40
	value, ok:=age["alice"]
	delete(age,"bob")
	for key,val: range age{

	}
	size:=len(age)
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter++ // Data race: multiple goroutines modifying 'counter' without synchronization
		}()
	}

	wg.Wait()
	fmt.Println("Final Counter:", counter)
}
