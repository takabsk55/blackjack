import random

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

    def reset(self):
        return Deck(self.semetary)