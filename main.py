from card import Card,Deck,Semetary,Field
from player import Player,Dealer

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def judge(playerhand,dealerhand):
    if playerhand > 21:
        winplayer="dealer"
        return winplayer
    if dealerhand > 21:
        winplayer = "player"
        return winplayer
    elif dealerhand > playerhand:
        winplayer = "dealer"
        return winplayer
    elif dealerhand < playerhand:
        winplayer = "player"
        return winplayer
    elif dealerhand == playerhand:
        winplayer = "draw"
        return winplayer

def liq(winplayer,bet):
    if winplayer=="dealer":
        return 0
    if winplayer=="player":
        return bet*2
    if winplayer=="bj":
        return bet+bet*1.2
    if winplayer=="draw":
        return bet


def setup():

    field=Field()

    player=Player(1000)

    dealer=Dealer()


    return field,player,dealer

def main(field,player,dealer):
    wincount=0
    roop=100000
    moneyhis=[]
    for i in range(roop):
        if player.money<0:
            print("burst")
            break
        winplayer=""
        #bet=player.pare_bet()
        #bet=player.marchin_bet()
        bet=player.bet()
        dealer.addhand(field.draw())

        player.addhand(field.draw())
        player.addhand(field.draw())

        while(True):
            if dealer.checkbj():
                winplayer="dealer"
                break
            if player.checkbj():
                winplayer="bj"
                break

            move=player.strategy(dealer.getSumHand())

            if move=="hit":
                player.addhand(field.draw())

            if move=="double":
                player.addhand(field.draw())
                player.money-=bet
                bet=bet*2
                move="stand"

            if move=="stand":
                playerhand=player.getSumHand()
                while(dealer.getSumHand()<17):
                    dealer.addhand(field.draw())
                dealerhand=dealer.getSumHand()
                winplayer=judge(playerhand,dealerhand)
                #print(playerhand)
                break
        if winplayer=="player" or winplayer=="bj":
            wincount+=1
        #print(winplayer)
        field.semetary.addSemetary(player.trashHand())
        field.semetary.addSemetary(dealer.trashHand())
        player.money+=liq(winplayer,bet)
        moneyhis.append(player.money)
        player.prebet=bet
        player.prewin=winplayer

    print(wincount/len(moneyhis))
    print(player.money)
    plt.plot(moneyhis)
    plt.savefig("his")


if __name__ == '__main__':
    field,player,dealer=setup()
    main(field,player,dealer)