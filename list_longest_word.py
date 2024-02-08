words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'head', 'of', 'the', 'lazy', 'dog.']
longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word

print(f'Longest word in list is "{longest_word}", {len(longest_word)} characters')
print(f'Shortest word in list is "{shortest_word}", {len(shortest_word)} characters')