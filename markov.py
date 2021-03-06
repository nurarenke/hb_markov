"""Generate markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    # your code goes here
    words = input_text.split()
    for i in range(len(words)-2):
        # chains[(words[i], words[i+1])] = [words[i+2]]
        key = (words[i], words[i+1])
        value = words[i+2]
        
        if key not in chains:
            chains[key] = [value]
        else:
            chains[key].append(value)

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    bigram = choice(chains.keys())
    # value = choice(chains[key])
    

    while bigram in chains.keys():
        bigram_first = bigram[0]
        bigram_second = bigram[1]
        value = choice(chains[bigram])

        words.append(bigram_first)
        words.append(bigram_second)
        words.append(value)
        
        bigram = (bigram_second, value)
        
 
    return " ".join(words)

    

filename = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(filename)

# # Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

#pseudo code making the dictionary:
# create a dictionary with the keys as the first two words
# pray that it turns into tuples
# grab the third word and save it as a value
# don't overwrite the value every time we find another instance, 
# save the values to a list
# creating a new list for every key
# if the key already exists, we do not have to create a new list

#pseudo code for generating random text:
# make a link with the two words from the key and the random word from the value list
# make a new key out of the second word from the previous key and...
# ...add the random word from the value list
# repeat