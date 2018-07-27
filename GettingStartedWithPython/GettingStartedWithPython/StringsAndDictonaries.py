# Exercise about Strings and Dictonaries from Kaggle tutorial site
# 0. About strings length
a = ""
length = 0

b = "it's ok"
length = 7

c = 'it\'s ok'
length = 7

d = """hey"""
length = 3

e = '\n'
length = 1

# 1.
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return (len(zip_code)==5 and zip_code.isdigit())

# 2.
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index_list = []
    for i,word in enumerate(doc_list):
        splited_wrds = word.split()
        normal_word = [wrd.rstrip('.,').lower() for wrd in splited_wrds]
        if keyword.lower() in normal_word:
            index_list.append(i)
    return index_list
# 3.
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    answer_tuple = {}
    for keyword in keywords:
        answer_tuple[keyword] = word_search(doc_list, keyword)
    return answer_tuple

# 4.
def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    
    s = ''
    # The characters currently being used to build the left and right half of 
    # the diamond, respectively. (We need to escape the backslash with another
    # backslash so Python knows we mean a literal "\" character.)
    l, r = '/', '\\'
    # The "radius" of the diamond (used in lots of calculations)
    rad = height // 2
    for row in range(height):
        # The first time we pass the halfway mark, swap the left and right characters
        if row == rad:
            l, r = r, l
        if row < rad:
            # For the first row, use one left character and one right. For
            # the second row, use two of each, and so on...
            nchars = row+1
        else:
            # Until we go past the midpoint. Then we start counting back down to 1.
            nchars = height - row
        left = (l * nchars).rjust(rad)
        right = (r * nchars).ljust(rad)
        s += left + right + '\n'
    # Trim the last newline - we want every line to end with a newline character
    # *except* the last
    return s[:-1]

# 5.
def conditional_roulette_probs(history):
    """
    Example: 
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5}, 
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """
    # dict where keys are numbers and values are dicts
    # counts[a][b] is the number of times we've spun the number b immediately after spinning a
    counts = {}
    # Iterate over the indices of history *except* the first (index 0). (In the loop, We'll 
    # be looking at each index alongside its previous index. But there's no previous index for i=0)
    for i in range(1, len(history)):
        # The numbers for the ith spin and the spin before it
        roll, prev = history[i], history[i-1]
        # If we haven't seen prev before, we need to add it to counts. (Otherwise counts[prev] will give a KeyError)
        if prev not in counts:
            counts[prev] = {}
        # Similar to above - add key to the inner dict if not present
        if roll not in counts[prev]:
            counts[prev][roll] = 0
        counts[prev][roll] += 1

    # We have the counts, but still need to turn them into probabilities
    probs = {}
    # dict.items() gives us a dictionary's (key, value) pairs as a sequence of tuples.
    for prev, nexts in counts.items():
        # The total number of spins that landed on prev (not counting the very last spin)
        total = sum(nexts.values())
        # Take the nects dictionary and normalize it so that its values sum to 1 (and represent probabilities)
        sub_probs = {next_spin: next_count/total
                for next_spin, next_count in nexts.items()}
        probs[prev] = sub_probs
    return probs
