import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
type(data)


def meaning(word):
    word=word.lower()
    v = get_close_matches(word, data.keys(), cutoff=0.75)
    if word in data:
        return data[word]
    elif len(v) > 0:
        z= input("Did you mean %s instead? Enter y if yes or n if no: " % v[0])
        if z == "y":
            return data[v[0]]
        elif z == "n":
            return "word not found"
        else:
            return "didnt understand. Try again"
            
    else:
        return "word not found"

x=input("Enter the word: ")

lst=meaning(x)
if type(lst)==str:
    print(lst)
else:
    for i in range(len(lst)):
        print(lst[i])
