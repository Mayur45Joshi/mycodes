#{ tiger, riget,rat,tra, deer,reed}

"""a = ("tiger, riget,rat,tra, deer,reed")

print(a.count("tiger"))
print(a.count("rat"))
print(a.count("deer"))"""

"""def count_jumbled_words(word_list):
    # Create a dictionary to store word counts
    word_counts = {}

    # Iterate through each word in the list
    for word in word_list:
        # Sort the characters in the word to create a unique key
        sorted_word = "".join(sorted(word))

        # Increment the count for the sorted word
        if sorted_word in word_counts:
            word_counts[sorted_word] += 1
        else:
            word_counts[sorted_word] = 1

    # Print the word counts
    for word, count in word_counts.items():
        if count > 1:
            print(f"Word: {''.join(sorted(word))}, Count: {count}")"""

from collections import defaultdict

word_list = ["listen", "silent", "enlist", "google", "gogole", "lives", "elvis", "viles"]
def count_jumbled_words(word_list):
    # Create a dictionary to store the count of each normalized word
    word_count = defaultdict(int)

    # Traverse each word in the input list
    for word in word_list:
        # Sort the word to create a normalized form
        normalized = ''.join(sorted(word))

        # Increment the count of the normalized word
        word_count[normalized] += 1

    return dict(word_count)

count_jumbled_words(word_list)
