from card import Card,Deck,Semetary

def setup():
    print("hoo")
    marks=["spade","heart","clover","diamond"]
    cards=[]
    for i in marks:
        for j in range(1,14):
            cards.append(Card(i,j))
    deck=Deck(cards)

    semetary=Semetary()

    deck.shuffle()
    print(deck.decknum())
    print(deck.draw().num)
    print(deck.decknum())


    return deck,semetary

def main():
    print("hoge")

if __name__ == '__main__':
    setup()
    main()