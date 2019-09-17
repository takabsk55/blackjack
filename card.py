import random

class Field():
    def __init__(self):
        marks = ["spade", "heart", "clover", "diamond"]*6
        cards = []
        for i in marks:
            for j in range(1, 14):
                cards.append(Card(i, j))

        self.deck = Deck(cards)
        self.semetary = Semetary()


    def checkdeck(self):
        if self.deck.decknum()<=0:
            self.deck=Deck(self.semetary.getsemetary())
            self.deck.shuffle()

    def draw(self):
        self.checkdeck()
        return self.deck.draw()

class Card():
    def __init__(self,mark,num):
        self.num=num
        self.mark=mark

class Deck():
    def __init__(self,cards):
        self.deck=cards

    def shuffle(self):
        random.shuffle(self.deck)

    def decknum(self):
        return len(self.deck)

    def draw(self):
        return self.deck.pop(0)

class Semetary():
    def __init__(self):
        self.semetary=[]

    def addSemetary(self,card):
        for i in range(len(card)):
            self.semetary.append(card[i])

    def getsemetary(self):
        return self.semetary
