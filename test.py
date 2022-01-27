import pandas as pd
import json
import random

count = 0
lines = None

compiledDictionary = {}

top_words = None
with open("google-10000-english-no-swears.txt") as file:
    top_words = file.readlines()
top_words_dict = set()
for word in top_words:
    top_words_dict.add(word.strip())


with open("words.txt") as file:
    lines = file.readlines()

for line in lines:
    words = [curr.strip() for curr in line.split(",")]
    if(words[0] in top_words_dict):
        if(len(words) <= 1):
            continue
        synonyms = []
        remaining = words[1:-1]
        for synonym in remaining:
            if(synonym in top_words_dict):
                synonyms.append(synonym)
        if(len(synonyms) <= 2):
            continue
        compiledDictionary[words[0]] = synonyms


target = random.choice(list(compiledDictionary.items()))[0]
start = random.choice(list(compiledDictionary.items()))[0]

print("Your start word is \"{}\"".format(start))
print("Your target word is \"{}\"".format(target))
print("Let's go from {} -> {}".format(start, target))
print("___________")

currWord = start
count = 0

while(True):
    if(currWord == target):
        print("CONGRATULATIONS!!!!!!")
        print("It only took you {} tries!".format(count))
        break
    count += 1
    print("Our current word is {}".format(currWord))
    print("Options:")

    options = compiledDictionary.get(currWord)
    random.shuffle(options)
    options = options[0:min(len(options), 7)]

    for i in range(0, len(options)):
        print("{}. {}".format(i, options[i]))
    val = input()
    currWord = options[int(val)]
