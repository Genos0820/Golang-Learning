package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

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

func main() {
	URL := "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"
	resp, err := http.Get(URL)
	if err != nil {
		log.Println("Error:", err)
		return
	}
	defer resp.Body.Close()
	var data jsonResponse
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error:", err)
		return
	}
	errs := json.Unmarshal(body, &data)
	if errs != nil {
		log.Println("Error in unmarshalling json:", err)
		return
	}

	for _, value := range data.Results {
		fmt.Println(value.Country)
	}
}
