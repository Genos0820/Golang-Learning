package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	deck := newDeck()
	if len(deck) != 52 {
		t.Errorf("Expected deck length of 52, but got %v", len(deck))
	}
	if deck[0] != "Ace of Spades" {
		t.Errorf("First Element is wrong")
	}
	if deck[len(deck)-1] != "King of Hearts" {
		t.Errorf("Last Element is wrong")
	}
}

func TestSaveToDeckAndNewDeckTestFromFile(t *testing.T) {
	os.Remove("_decktesting")
	deck := newDeck()
	deck.saveToFile("_decktesting")
	loadedDeck := newDeckFromFile("_decktesting")
	if len(loadedDeck) != 52 {
		t.Errorf("Expected deck length of 52, but got %v", len(deck))
	}
	os.Remove("_decktesting")
}
