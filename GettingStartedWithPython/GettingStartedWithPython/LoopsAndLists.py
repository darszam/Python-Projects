# Exercise about Loops and lists from Kaggle tutorial site
# 1.
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False
print(has_lucky_number([1,2,2]))

def has_lucky_number_one_line(nums):
    return any([num % 7 == 0 for num in nums])
print(has_lucky_number_one_line([2,5,7,3,2]))

# 2.
# [1, 2, 3, 4] > 2 # Compile error

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [ele > thresh for ele in L]

# Second solution
def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

# 3.
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

# 4.
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    sum_value = 0
    for i in range(n_runs):
        sum_value +=play_slot_machine()
    return (sum_value-n_runs)/n_runs
estimate_average_slot_payout(100000)

# 5.
def slots_survival_probability(start_balance, n_spins, n_simulations):
    """Return the approximate probability (as a number between 0 and 1) that we can complete the 
    given number of spins of the slot machine before running out of money, assuming we start 
    with the given balance. Estimate the probability by running the scenario the specified number of times.
    
    >>> slots_survival_probability(10.00, 10, 1000)
    1.0
    >>> slots_survival_probability(1.00, 2, 1000)
    .25
    """
    # How many times did we last the given number of spins?
    successes = 0
    # A convention in Python is to use '_' to name variables we won't use
    for _ in range(n_simulations):
        balance = start_balance
        spins_left = n_spins
        while balance >= 1 and spins_left:
            # subtract the cost of playing
            balance -= 1
            balance += play_slot_machine()
            spins_left -= 1
        # did we make it to the end?
        if spins_left == 0:
            successes += 1
    return successes / n_simulations