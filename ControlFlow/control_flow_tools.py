x = 0

# if statement
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

# for statement
words = ["cat", "dog", "tiger"]
for word in words:
    print(word, len(word))

# modifying the iterable
for word in words[:]:
    if len(word) > 3:
        words.append(word)

print(words)

# the range function
for i in range(1, 100, 10):
    print(i)
