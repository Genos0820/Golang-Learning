package handlers

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

var items = []int{1, 2, 3}

func GetItem(c *gin.Context) {
	c.JSON(200, gin.H{"message: Items retrieved": items})
}

func CreateItem(c *gin.Context) {
	var item int
	err := c.ShouldBindJSON(&item)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"Errors": err.Error()})
		return
	}
	items = append(items, item)
	log.Printf("it comes")
	c.JSON(http.StatusCreated, item)
}
