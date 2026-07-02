"""
Project: Word Counter
Author: Mocherla Kasthuri
Description: Counts words, characters, sentences, and displays word frequency.
"""

text = input("Enter a paragraph:\n")

words = text.split()

word_count = len(words)
character_count = len(text)
sentence_count = text.count(".") + text.count("!") + text.count("?")

print("\n===== Analysis =====")
print(f"Words: {word_count}")
print(f"Characters: {character_count}")
print(f"Sentences: {sentence_count}")

frequency = {}

for word in words:
    word = word.lower().strip(".,!?")
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
