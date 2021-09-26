from card import Card
import random, time

def create_deck():
    deck = []
    suits = ["spades", "hearts", "diamonds", "clubs"]

    for val in range(13):
        for suit in suits:
            deck.append(Card(val + 1, suit))

    return deck

def deal_deck(deck):
    player_1_hand = []
    player_2_hand = []
    for i, card in enumerate(deck):
        # Even iterations go to player 1
        # Odd iterations go to player 2
        if i % 2 == 0:
            player_1_hand.append(card)
        else:
            player_2_hand.append(card)
    
    return player_1_hand, player_2_hand
    

if __name__ == "__main__":
    start_time = time.time()
    # Create, shuffle, and deal deck
    deck = create_deck()
    random.shuffle(deck)
    hand1, hand2 = deal_deck(deck)

    iterations = 0
    while len(hand1) > 0 and len(hand2) > 0:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)

        # Player 1 wins battle
        if card1.value > card2.value:
            hand1.append(card1)
            hand1.append(card2)
        
        # Player 2 wins battle
        elif card1.value < card2.value:
            hand2.append(card1)
            hand2.append(card2)
        
        # WAR (players battled with the same value card)
        else:
            war_cards = []
            war_cards.append(card1)
            war_cards.append(card2)

            while True:
                # Each player discards 3 cards
                # 4th card is compared
                try:
                    war_cards.append(hand1.pop(0))
                    war_cards.append(hand1.pop(0))
                    war_cards.append(hand1.pop(0))
                    war_card1 = hand1.pop(0)
                    war_cards.append(war_card1)

                    war_cards.append(hand2.pop(0))
                    war_cards.append(hand2.pop(0))
                    war_cards.append(hand2.pop(0))
                    war_card2 = hand2.pop(0)
                    war_cards.append(war_card2)
                except IndexError:
                    break

                # Tie (war again)
                if war_card1.value == war_card2.value:
                    continue
                
                # Player 1 wins war
                elif war_card1.value > war_card2.value:
                    hand1.extend(war_cards)
                
                # Player 2 wins war
                else:
                    hand2.extend(war_cards)
                
                break

    
        iterations += 1

        if time.time() - start_time > 15:
            break

    # Player 1 wins
    if len(hand2) == 0:
        print(f"Player 1 won after {iterations} iterations in {time.time() - start_time} seconds.")
    
    # Player 2 wins
    elif len(hand1) == 0:
        print(f"Player 2 won after {iterations} iterations in {time.time() - start_time} seconds.")

    # Game timed out
    else:
        print(f"The game timed out after {iterations} iterations in {time.time() - start_time} seconds, the score was {len(hand1)} vs {len(hand2)}.")