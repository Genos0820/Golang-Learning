package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

// This file is a standalone Gin-based server. To run it without touching
// the repository's existing `main.go`, use:
//
//   go run gin_app.go
//
// Note: if you build the whole package (go build .) and there are other
// files with a `main` function in the same package, you'll get duplicate
// symbol errors. Use `go run gin_app.go` to run only this file.

type jsonResponse struct {
	Count          int      `json:"Count"`
	Message        string   `json:"Message"`
	SearchCriteria any      `json:"SearchCriteria"`
	Results        []result `json:"Results"`
}

type result struct {
	Country        string          `json:"Country"`
	Mfr_CommonName string          `json:"Mfr_CommonName"`
	Mfr_ID         int             `json:"Mfr_ID"`
	Mfr_Name       string          `json:"Mfr_Name"`
	VehicleTypes   []vehiclesTypes `json:"VehicleTypes"`
}

type vehiclesTypes struct {
	IsPrimary bool   `json:"IsPrimary"`
	Name      string `json:"Name"`
}

func fetchManufacturers() (jsonResponse, error) {
	URL := "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"
	resp, err := http.Get(URL)
	if err != nil {
		return jsonResponse{}, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return jsonResponse{}, err
	}

	var data jsonResponse
	if err := json.Unmarshal(body, &data); err != nil {
		return jsonResponse{}, err
	}

	return data, nil
}

func main() {
	r := gin.Default()

	// returns the full JSON from the external API
	r.GET("/manufacturers", func(c *gin.Context) {
		data, err := fetchManufacturers()
		if err != nil {
			log.Println("fetch error:", err)
			c.JSON(http.StatusBadGateway, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, data)
	})

	// returns only the list of countries from the Results array
	r.GET("/countries", func(c *gin.Context) {
		data, err := fetchManufacturers()
		if err != nil {
			log.Println("fetch error:", err)
			c.JSON(http.StatusBadGateway, gin.H{"error": err.Error()})
			return
		}
		countries := make([]string, 0, len(data.Results))
		for _, v := range data.Results {
			countries = append(countries, v.Country)
		}
		c.JSON(http.StatusOK, gin.H{"countries": countries})
	})

	// default listens on :8080
	if err := r.Run(); err != nil {
		log.Fatalf("server error: %v", err)
	}
}
