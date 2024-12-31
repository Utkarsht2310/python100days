import random

# Function to deal a card
def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 for J, Q, K; 11 for Ace
    return random.choice(cards)

# Function to calculate the score
def calculate_score(cards):
    """Calculate the score from the list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function to compare scores
def compare(player_score, dealer_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

# Main game logic
def blackjack_game():
    print("Welcome to Blackjack!")

    # Deal initial cards
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

# Run the game
blackjack_game()
