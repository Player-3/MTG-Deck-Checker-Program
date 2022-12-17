deck1 = {""}
deck2 = {""}
matchingCards = {}
diffCards = {}
print("Welcome to the deck checker program!")
print("This program will check two decks and tell you which cards are in both decks and which cards are in only one deck.")
print("Please enter the name of the first deck.")
firstDeckName = input()
print("Please enter the name of the second deck.")
secondDeckName = input()

with open (firstDeckName+".txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        deck1.add(line)
with open (secondDeckName+".txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        deck2.add(line)

f.close()

matchingCards = deck1.intersection(deck2)
diffCards = deck1.difference(deck2)

with open ("matchingCards.txt", "w") as k:
    for card in matchingCards:
        k.write(card + "\n")

with open ("diffCards.txt", "w") as k:
    for card in diffCards:
        k.write(card + "\n")
        
k.close()