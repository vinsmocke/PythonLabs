from math import factorial

def count_anagrams(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    anagram_count = factorial(len(word))
    for count in letter_count.values():
        anagram_count //= factorial(count)

    return anagram_count

word = input("Введіть слово: ").strip()

print(f"Кількість анаграм: {count_anagrams(word)}")
