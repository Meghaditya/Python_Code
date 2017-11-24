# looping over dictionaries
dictionary = {'One': 1, 'Two': 2}
for k, v in dictionary.items():
    print(k, v)

# retrieving position index and content
for i, v in enumerate(['cat', 'dog', 'tiger']):
    print(i, v)

# loop over two sequences using zip()
qs = ["name", "age", "location"]
ans = ["meghaditya", "27", "howrah"]

for q, a in zip(qs, ans):
    print("Question is {0}, answer is {1}".format(q, a))

# iterate over a range in reversed order
for i in reversed(range(1, 10, 4)):
    print(i)

for w in sorted(qs):
    print(w)

# tempting thing to do
for q in qs[:]:
    if len(q) > 5:
        qs.remove(q)

print(qs)
