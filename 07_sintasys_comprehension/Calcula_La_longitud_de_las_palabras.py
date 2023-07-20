def count_words_by_length(words):
  return {len(word): sum(1 for w in words if len(w) == len(word)) for word in words}

response = count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

print(response)


from collections import defaultdict

def count_words_by_length(words):
    word_lengths = defaultdict(int)
    for word in words:
        word_lengths[len(word)] += 1
    return dict(word_lengths)


words = ["apple", "banana", "orange", "grapefruit", "pear", "kiwi"]
result = count_words_by_length(words)
print(result)
# Salida: {5: 2, 6: 2, 7: 1, 10: 1}
