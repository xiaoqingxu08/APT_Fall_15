# from Adam Barr's wonderful book "Find the Bug"

''' This function draws a car from a deck and puts it into a hand. It is
meant to be part of the game Go Fish, so if the resulting hand has all four 
suits for a given card rank, those four cards are removed from the hand. 

Cards are identified by their rank and suit: the rank is one of the elements
in the list ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
and the suit is on of the elements of the list ["spades", "hearts", "diamonds", "clubs"].

A deck is a list that initially contains 52 elements. Each element of the list
is a tuple with two elements: the rank and the suit. So a single entry
in the deck might be the tuple ("K", "spades"), which is the king of spades.

A hand is a dictionary. In each element of the dictionary, the key is
the rank and the value is a list that contains the names of the suits that the hand
holds for that rank. E.g., if a hand as the 3 of spades and the 3 of hearts, and
no other 3s, then the key "3" has the value ["spades", "hearts"]. A key should not
have an empty list associated with it - if no cards of a given rank are held,
no value exists for that key.'''

import random

def getCard(deck):

  ''' Randomly remove a single card from the deck and return it. Assumes that the deck 
      is not empty.

      deck: A deck as described above

      Returns: a single card, which is a tuple with two elements, the rank and the suit

  '''

  index = int (len(deck) * random.random())
  newCard = deck[index]
  del deck[index]
  return newCard

def drawCard(name, deck, hand):

  ''' Draw a new card from the deck and add it to the hand. If the hand now holds the rank
      in all four suits, then remove them from the hand.

      name: A string with the name of the playerHand, used on for display purposes.
      deck: A deck as described above
      hand: A hand dictionary as described above

      Returns: None.
  '''

  if len(deck) > 0: # protect against empty deck
    newCard = getCard(deck)
    cardRank = newCard[0]
    cardSuit = newCard[1]

    if cardRank in hand:
      # append this suit to the result
      hand[cardRank].append(cardSuit)
      #if len(hand) == 4:
      if len(hand[cardRank]) == 4:
        print name, "lay down", cardRank + "s"
        del hand[cardRank]

    else:
      # first of this suit, create a list with one element
      hand[cardRank] =  [ cardSuit ]

def main():
  deck = [("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades"), ("J", "spades"), ("Q", "spades"), ("K", "spades"), ("A", "spades"), 
          ("2", "hearts"), ("3", "hearts"), ("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts"), ("9", "hearts"), ("10", "hearts"), ("J", "hearts"), ("Q", "hearts"), ("K", "hearts"), ("A", "hearts"),
          ("2", "diamonds"), ("3", "diamonds"), ("4", "diamonds"), ("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds"), ("10", "diamonds"), ("J", "diamonds"), ("Q", "diamonds"), ("K", "diamonds"), ("A", "diamonds"),
          ("2", "clubs"), ("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs"), ("8", "clubs"), ("9", "clubs"), ("10", "clubs"), ("J", "clubs"), ("Q", "clubs"), ("K", "clubs"), ("A", "clubs")]
  
  players = ["Tom", "Jim", "Paul", "David"]
  hands = [{}, {}, {}, {}]

  while(len(deck) >0):
    for p_id in xrange(2):
      drawCard(players[p_id], deck, hands[p_id])
      if (len(deck) == 0): break

  return 

if __name__ == "__main__":
  main()
