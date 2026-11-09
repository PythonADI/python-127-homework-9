def count_words(words):
    """Return a dictionery with the count of each in the list."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
def most_common(counts):
    """Return a tuple(word, count) for the most frequent word without using max()."""
    if not counts:
        return None
    most_frequent_word = None
    max_count = -1 
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
    return(most_frequent_word, max_count)
words = ["the","cat", "and", "the", "dog", "and", "the", "bird"]
counts = count_words(words)
print(counts)

word, times = most_common(counts)
print(f"Most common:{word} ({times} times)")   
print(most_common({"a": 2, "b": 2}))
print(count_words([]))         