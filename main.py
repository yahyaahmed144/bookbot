from stats import wordsList
from stats import countWords

path = "/home/yahya/Desktop/Workspace/yahya/bookbot/bookbot/books/frankenstein.txt"

words = wordsList(path);
# returns a list of all words ["this", "is", "a", "book"]
char_count = {};

for word in words:
    for char in word:
        char_count[char.lower()] =char_count.get(char.lower(), 0) +1

    
print("============ BOOKBOT ============")
print("----------- Word Count ----------")
print(f"Found {countWords(path)} total words")
print("--------- Character Count -------")

for key in sorted(char_count):
    print(f"{key} : {char_count[key]}")

print("============= END ===============")

