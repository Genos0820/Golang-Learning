package handlers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

var items = []int{1, 2, 3}

func GetItems(c *gin.Context) {
	c.JSON(http.StatusAccepted, gin.H{"Item retrieved": items})
}

type ItemRequest struct {
	Item int `json:"item"`
}

func CreateItem(c *gin.Context) {
	var req ItemRequest
	err := c.ShouldBindJSON(&req)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"Item can not be created": req.Item})
		return
	}
	items = append(items, req.Item)
	c.JSON(http.StatusCreated, req.Item)
}

/*
$headers = @{ "Content-Type" = "application/json" }
$body = '{"item":5}'
Invoke-WebRequest -Uri http://localhost:8080/items -Method POST -Headers $headers -Body $body
*/