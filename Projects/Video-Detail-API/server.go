package main

import (
	"io"
	"os"

	"gilab.com/progmaticreviews/golang-gin-poc/controller"
	"gilab.com/progmaticreviews/golang-gin-poc/middlewares"
	"gilab.com/progmaticreviews/golang-gin-poc/service"
	"github.com/gin-gonic/gin"
	gindump "github.com/tpkeeper/gin-dump"
)

var (
	videoService    service.VideoService       = service.New()
	VideoController controller.VideoController = controller.New(videoService)
)

func setupLogOutput() {
	f, _ := os.Create("gin.log")
	gin.DefaultWriter = io.MultiWriter(f, os.Stdout)
}

func main() {
	setupLogOutput()

	server := gin.New()
	server.Use(gin.Recovery(), middlewares.Logger(), middlewares.BasicAuth(), gindump.Dump())

	server.GET("/posts", func(ctx *gin.Context) {
		ctx.JSON(200, VideoController.FindAll())
	})
	server.POST("/posts", func(ctx *gin.Context) {
		ctx.JSON(201, VideoController.Save(ctx))
	})
	server.Run(":8080")
}
