def count_letters(word):
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter ,0) + 1
    return counts

print(count_letters("banana"))
print(count_letters("a"))
print(count_letters(""))


