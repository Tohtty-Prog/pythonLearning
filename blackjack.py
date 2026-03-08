import random

def makeDeck():
    suits = ['♥','♦','♣','♠']
    faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    deck = []

    for suit in suits:
        for face in faces:
            card = {
                "Suit": suit,
                "Face": face
            }
            deck.append(card)
    random.shuffle(deck)
    return deck

def hands(deck):
    p1_hand = []
    p2_hand = []
    for _ in range(2):
        p1_hand.append(deck.pop())
        p2_hand.append(deck.pop())
    return p1_hand,p2_hand

def calc_hands(hand):
    total = 0
    aces = 0
    for card in hand:
        if card["Face"] in ['K','J','Q']:
            total += 10
        elif card["Face"] == 'A':
            total += 11
            aces += 1
        else:
            total += int(card["Face"])
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def hit_stand(p1,p2, deck):
    p1_total = calc_hands(p1)
    p2_total = calc_hands(p2)

    while p1_total < 21:
        choice = input("Do u want to hit(H) or stand(S): ").lower()
        if choice == 's':
            break
        elif choice == 'h':
            p1.append(deck.pop())
            p1_total = calc_hands(p1)
            print(f"Cards: {p1}. Your total is {p1_total}")

    while p2_total < 17:
        p2.append(deck.pop())
        p2_total = calc_hands(p2)
    return p1_total, p2_total

deck = makeDeck()

p1_hand,p2_hand = hands(deck=deck)

p1_total = calc_hands(p1_hand)
p2_total = calc_hands(p2_hand)

print(f"Cards:{p1_hand} Total:{p1_total}")
print(f"Cards:{p2_hand} Total:{p2_total}")

p1_total,p2_total = hit_stand(p1=p1_hand,p2=p2_hand,deck=deck)

print(f"\nFinal Player hand: {p1_hand} Total: {p1_total}")
print(f"Final Dealer hand: {p2_hand} Total: {p2_total}")

if p1_total > 21:
    print("Player busts! Dealer wins.")
elif p2_total > 21:
    print("Dealer busts! Player wins.")
elif p1_total > p2_total:
    print("Player wins!")
elif p2_total > p1_total:
    print("Dealer wins!")
else:
    print("It's a tie!")

