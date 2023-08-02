def count_letters(phrase):
    letter_count = {}

    for letter in phrase:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count

phrase = "Hola mundo"
result = count_letters(phrase)
print(result)
# Salida:
# {
#   'H': 1,
#   'o': 2,
#   'l': 1,
#   'a': 1,
#   ' ': 1,
#   'm': 1,
#   'u': 1,
#   'n': 1,
#   'd': 1
# }
