def count_words(text):
    counts = {}
    for word in text.lower().split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

x = count_words("the cat and the hat")
print(x)