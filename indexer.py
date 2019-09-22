from typing import List, Set


def indexer(string: str, words: List[str]):
    # Build a word set so that we can quickly see whether the next chunk of
    # the given string is in the remaining collection of words
    word_set = {word for word in words}

    # Use an accumulator to store the starting indices of valid substrings
    accumulator: Set[int] = set()

    # Rely on the guarantee that "each word is the same length"
    #
    # We will use this to our advantage in validating the next chunk of the
    # given string.
    word_length = len(words[0])

    # Test every index of the given string
    for i in range(len(string)):
        if descend(string=string, i=i, word_set=word_set, word_length=word_length):
            accumulator.add(i)

    return accumulator


def descend(string: str, i: int, word_set: Set[str], word_length: int):
    # Handle our base case; if we're here we've used every word in the word list
    # exactly once
    if len(word_set) == 0:
        return True

    # Handle indexing errors
    elif i >= len(string):
        return False

    # Continue to recurse
    else:
        # Bite off the next chunk of the given word.
        #
        # Unfortunately, in Python this instantiates a new string, rather
        # than doing memory-clever referencing.
        # https://stackoverflow.com/q/49122407/11280049
        next_word = string[i:i + word_length]

        # At least we have constant lookup time for whether this new chunk is
        # the next step in a valid substring.
        if next_word in word_set:
            # If we have a match:
            # 1) Instantiate a new set without this word in it,
            # 2) Advance the given index by the known word length, and
            # 3) Continue to recurse
            smaller_word_set = word_set - {next_word}
            return descend(string, i + word_length, smaller_word_set, word_length)

    # We didn't find a match
    return False
