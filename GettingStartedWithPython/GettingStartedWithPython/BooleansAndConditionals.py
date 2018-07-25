# Exercise is from kaggle's python tutorial

# 1. Defining sign function - which takes a numerical argument and returns -1 
# if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(x):
    if(x>0): 
        return 1
    elif(x<0):
        return -1
    else:
        return 0

# 2. if expression in print
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies==1 else "candies")
    return total_candies % 3

to_smash(91)

to_smash(1)

# 3. Finding bugs
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)
# Printing False where we don't have umbrella, there is no rain, we don't have a hood and it's not workday
# That's because Python parenthesizes (not (rain_level > 0)) and is_workday instead of (not (rain_level > 0 and is_workday))

# 4. is_negative functions
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number<0 # Your code goes here (try to keep it to one line!)

# 5. hot dog order
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup&mustard&onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return ketchup ^ mustard

# 6. Calling bool() on an integer
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup+mustard+onion)==1

# 7. Simplified Blackjack
def should_hit(player_total, dealer_total, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
    return player_total<dealer_total