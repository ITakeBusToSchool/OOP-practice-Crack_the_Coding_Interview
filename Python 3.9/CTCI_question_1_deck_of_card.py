import random


# Step1: Prepare out classes:
# we will have three classes. Card, Deck, Player.
# Each of these will inherit fro, the onject.
# we create an init method for each class

class Card:
    def __init__(self,suit,val):
    # Step2: Create our class Card:
    # The Card is going to take a suit and value self. We're going to create the 
    # attributes suit, value and set them equal to whatever we pass in when we 
    # create a card
        self.suit=suit
        self.value=val
    
    # Create another method to show the card
    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
class Deck:
    def __init__(self):
        # Step3: Create our class Deck
        self.cards=[]
        self.build()
    # we create a build method which takes in self, 
    # and we want to create the 52 cards of 4 suits. 
    # We create a for loop that will loop "suit" through
    # ["Spades","Clubs", "Diamonds", "Hearts"]
    
    # we create another for loop with in the first for loop 
    # that will loop through values in range(1,14)
    def build(self):
        for s in ["Spades","Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
    
    # show method to show the self.card
    def show(self):
        for c in self.cards:
            c.show()
    # Step4 : Create a Shuffle method
    # we would probably like to suffle our deck. we import random
    # to use the "Fisher Yates Shuffle" which is a very neat shuffing 
    # algorithm that makes sure that each card has an equal likelihood of 
    # ending up in every other position
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

    ##method Drawing a card on the top
    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand=[]
    
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
        


#Test the Card class
# card= Card("yes",2)
# card.show()

#Test the Deck class
# deck=Deck()
# deck.show()
# print("Now, shuffle the deck")
# deck.shuffle()
# deck.show()


#Test for all class
deck=Deck()
deck.shuffle()

bob = Player("Bob")
bob.draw(deck)
bob.showHand()