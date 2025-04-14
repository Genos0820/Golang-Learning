package main

//"fmt"

func main() {
	// var card string = "Ace of Spades"
	// l := newcard()
	// cards := deck{"Five of Diamonds", newcard()}
	// cards = append(cards, "g")
	// fmt.Println(card, l, cards)
	// cards.print()
	deck1 := newDeck()
	//hand, deck1 := deal(deck1, 3)
	//hand.print()
	//deck1.print()
	//fmt.Printf("deck1.toString(): %v\n", deck1.toString())
	//deck1.saveToFile("deck1")
	//readDeck := newDeckFromFile("deck")
	//readDeck.print()
	deck1.shuffle()
	deck1.print()
}

// func newcard() string {
// 	card := "Ace of Spades"
// 	return card
// }
