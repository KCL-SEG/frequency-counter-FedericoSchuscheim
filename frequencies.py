"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        stringItem = str(item)
        if frequencies.get(stringItem) != None:
            frequencies[stringItem] += 1
        else:
            frequencies[stringItem] = 1
    return frequencies
