'''En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras 
que contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. 
La función debe devolver una nueva lista que contenga todas las palabras de la lista original que cumplan con 
la condición mencionada anteriormente. 
En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.'''

def find_words_with_two_vowels(words):
    def count_vowels(word):
        vowels = "aeiouAEIOU"
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count

    words_with_two_vowels = [word for word in words if count_vowels(word) == 2]
    return words_with_two_vowels

words1 = ["apple", "banana", "grape", "orange", "melon"]
words2 = ["hello", "world", "Python", "programming", "language"]
words3 = ["dog", "cat", "bird", "fish", "elephant"]

result1 = find_words_with_two_vowels(words1)
result2 = find_words_with_two_vowels(words2)
result3 = find_words_with_two_vowels(words3)

print(result1)  
print(result2)  
print(result3)  


