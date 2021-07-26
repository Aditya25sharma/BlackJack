import random
import cards_graphics
from os import system
from art import logo
system('clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #cards to be dealt with, 11 is ace, 10 equals J,K,Q

u_cards={"Values":[], "Rank":[],"Suit":[],"Sum":0}; #card's ranks and suit of user
c_cards={"Values":[], "Rank":[],"Suit":[],"Sum":0} #card's ranks and suits of computer

def player_cards(player): #gives a new card to players
  value=random.choice(cards)
  rank=face(value)
  suit=random.choice(['Spades', 'Diamonds', 'Hearts', 'Clubs'])
  
  player["Values"].append(value)
  player["Rank"].append(rank)
  player["Suit"].append(suit)
  player["Sum"]=total_score(player)
  return player

def face(value):  #provides a rank to card
  rank_type= value
  if(value==11):
      rank_type='A'
  elif(value==10):
      rank_type=random.choice(['10', 'J', 'K', 'Q'])

  return(rank_type)


def total_score(player):
  scores = sum(player["Values"])   #adding cards
  if(11 in player["Values"] and scores>21): #if a card is Ace and sum goes beyond 21
    scores-=10
    index=player["Values"].index(11)
    player["Values"[index]]=1 #the value of ace there is 1 now
  return(scores)
    

def show_card(player, index=-1): #-1 index means top card, shows all cards otherwise
  if(index != -1):
    for i in range(len(player["Rank"])):
      print(f"{player['Rank'][i]} of {player['Suit'][i]}")
      cards_graphics.card_display(player["Rank"][i], player["Suit"][i])
  else:
    print(f"{player['Rank'][-1]} of {player['Suit'][-1]}")
    cards_graphics.card_display(player["Rank"][-1], player["Suit"][-1])

def hide_card(): #opp. side of card
  print(cards_graphics.HIDDEN_CARD)

def result_disp(): #displays result in the end
  print("Your cards: ")
  show_card(u_cards, 0)
  print(f"Your score: {u_cards['Sum']}\n")
  print("Computer's cards: ")
  show_card(c_cards, 0)
  print(f"Computer's score: {c_cards['Sum']}\n")

################################################################################
print(logo) #game satrts here

play = input("Do you want to play Blackjack?. Type y or n: ")

if(play=='y'):
  player_cards(c_cards)
  print("Computer first card:" ) 
  show_card(c_cards)
  hide_card()
  
  print(f"Computer's current score: {c_cards['Sum']} + ?...\n")
  player_cards(u_cards)
  print("Your first card:" )
  show_card(u_cards)

  while(play=='y' and u_cards['Sum']<21): #till the user want to take cards without succeeding 21
    player_cards(u_cards)
    print("You got ")
    show_card(u_cards)
    print(f"Your Current score: {u_cards['Sum']} | Computer's current score: {c_cards['Sum']} + ?...\n")

    if(u_cards['Sum']>21): # sum>21
      player_cards(c_cards)
      result_disp()
      print("You went over. You lose")

    elif(u_cards['Sum']==21): # sum=21
      player_cards(c_cards)
      result_disp()
      print("BlackJack. You won!")

    else: 
      play = input("Type y to get another card, type n to pass ") # another card choice
      system('clear')
      if(play=='n'): # user do not want to continue
        while(c_cards['Sum']<=17): # computer plays till its sum is <17
          player_cards(c_cards)
        result_disp()

        if(c_cards['Sum']>21): 
          print("Computer got greedy! You won")

        elif(u_cards['Sum']>c_cards['Sum'] ):         
          print("Yay! You Won :)")

        elif(u_cards['Sum']==c_cards['Sum']):  
          print("Damn! A Draw!")

        else:
          print("Bad Luck. You lost")
          
else:
  print("Nice meeting you")