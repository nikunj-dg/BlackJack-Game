#--------------FNS-----------------#

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

class Hand:
    def __init__(self,name):
        self.name = name
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces 
        self.balance = 1000  # start with 1000 balance
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hand.add_card(deck.deal_one())

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)    

#------------------MAIN-------------------#

# Initail Condition
balance = 1000

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until it reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_one = Hand('One')
    player_one.add_card(deck.deal_one())
    player_one.add_card(deck.deal_one())
    
    dealer_hand = Hand('Dealer')
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    player_one.balance = balance
    print(f"{player_one.name} has {player_one.balance} in balance.\n")
    bet = int(input("Enter the bet amount : "))
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_one,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_one) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_one,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_one.value > 21:
            print("Player busts!")
            player_one.balance -= bet
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_one.value <= 21:
        
        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal_one())    
    
        # Show all cards
        show_all(player_one,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            print("Dealer busts!")
            player_one.balance += bet

        elif dealer_hand.value > player_one.value:
            print("Dealer wins!")
            player_one.balance -= bet

        elif dealer_hand.value < player_one.value:
            print("Player wins!")
            player_one.balance += bet

        else:
            print("Dealer and Player tie! It's a push.")        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_one.balance)
    balance = player_one.balance
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
    
