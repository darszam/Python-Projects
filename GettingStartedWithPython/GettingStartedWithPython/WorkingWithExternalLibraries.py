# Exercise about working with external libraries from Kaggle tutorial site

# 1.
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    # Format those values into strings beginning with dollar sign
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    # Set the new labels
    graph.set_yticklabels(new_labels)
graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

# 2.
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# 3.
def hand_total(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total_first_hand = hand_total(hand_1)
    total_second_hand = hand_total(hand_2)
    return total_first_hand <= 21 and (total_first_hand > total_second_hand or total_second_hand > 21)

# 4.
def my_agent(wheel):
    last_number = 0
    while wheel.num_remaining_spins() > 0:
        if last_number == 5:
            # Unlucky! Don't bet anything.
            guess = none
        else:
            guess = random.randint(0, 10)
        last_number = wheel.spin(number_to_bet_on=guess)
