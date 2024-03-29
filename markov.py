"""Generate Markov text from text files."""

from random import choice
def open_and_read_file(file    """Take file path as string;     Takes a string that is a f    the file's contents as on    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for index in range(len(words)-2):
        key = words[index], words[index+1]
        value = words[index + 2]
        if key not in chains:
            chains[key] = [value]
               
        else: 
            chains[key].append(value)

            #if key is already in chains, append value to value_list
            #if key is not already in chains, make value_list with value (as the only value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # Step1 : pick a random key
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]

    while key in chains: 
        
    # Step 2: Choose a next word
        chosen_word = choice(chains[key])
        words.append(chosen_word)
    #Step 3: Make a new key
        key = (key[1], chosen_word)

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
