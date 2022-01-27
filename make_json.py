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
