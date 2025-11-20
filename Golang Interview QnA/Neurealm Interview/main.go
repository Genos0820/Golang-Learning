package main

import (
	"errors"
	"fmt"
)

//Implent a queue using interface
//Learn about pointer and struct and interface in go

type Queue interface {
	Enqueue(item interface{}) error
	Dequeue() (interface{}, error)
	Peek() (interface{}, error)
	Size() int
	IsEmpty() bool
	IsFull() bool
}

type ArrayQueue struct {
	items    []interface{}
	capacity int
}

func NewArrayQueue(capacity int) *ArrayQueue {
	if capacity <= 0 {
		capacity = -1
	}
	return &ArrayQueue{
		items:    make([]interface{}, 0),
		capacity: capacity,
	}
}

func (q *ArrayQueue) Enqueue(item interface{}) error {
	if q.IsFull() {
		return errors.New("Queue is full")
	}
	q.items = append(q.items, item)
	return nil
}

func (q *ArrayQueue) Dequeue() (interface{}, error) {
	if q.IsEmpty() {
		return nil, errors.New("Queue is empty")
	}
	val := q.items[0]
	q.items = q.items[1:]
	return val, nil
}

func (q *ArrayQueue) IsEmpty() bool {
	if q.Size() == 0 {
		return true
	}
	return false
}

func (q *ArrayQueue) IsFull() bool {
	if q.capacity == -1 {
		return false // Unlimited queue is never full
	}
	return len(q.items) >= q.capacity
}
func (q *ArrayQueue) Size() int {
	return len(q.items)
}

func (q *ArrayQueue) Peek() (interface{}, error) {
	if q.IsEmpty() {
		return nil, errors.New("Queue is empty")
	}
	val := q.items[0]
	return val, nil
}

func main() {
	bQ:=NewArrayQueue(4)
	bQ.Enqueue(3)
	bQ.Enqueue("apex")
	fmt.Println(bQ)
}
