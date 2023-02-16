# This is about to be a fun and messy time
# TODO: Move all this stuff into a utils thing or whatever and clean it up

import json
import time
import gensim
from gensim.models import KeyedVectors

# Change this if you want to load a new model
modelName = "./model/" + "word2vec.model"

# Load in the model- see README for download link
try:
    print("Attempting to load existing gensim model...")
    model = KeyedVectors.load(modelName)
    print("Loaded existing gensim model!")
except:
    print("Didn't find one!\nLoading the given model for the first time...")
    start = time.time()
    # And change this path to your other model or whatever
    model = gensim.models.KeyedVectors.load_word2vec_format(
        './model/GoogleNews-vectors-negative300.bin', binary=True)
    totalSeconds = time.time() - start
    print("First time model loaded in", totalSeconds,
          "seconds.")
    model.save(modelName)

# Now begins the actual fun stuff :)

fiveWords = input("Please give your five codenames words, space separated: ")
# TODO: Actual validation, but this primitive loop will do for now
while True:
    if len(fiveWords.split(" ")) != 5:
        fiveWords = input(
            "Let's try again... please give your five codenames words, space separated:")
        print(fiveWords.split(" "))
    else:
        break
wordSplit = fiveWords.split(' ')
# TODO: Error check for words not in the vocabulary- should be a simple O(1) map check
# TODO: Ensure no duplicate words (simple len(set(wordSplit)) == len(wordSplit)), may need to convert all to lowercase
print(f"Gottem'! Your five words are {wordSplit}")

# TODO: 1. Get all codenames words so you can avoid false hints
# TODO: 2. Get the assassin word so you can give that a 10x weight of things to avoid

# TODO: Ensure duplicates are filtered out at the end...? (i.e. "white" and "_White")

# Grab the most similar words of all the words in the wordSplit list
# I'd be shocked if more than 40 words were > .49, but also there's GOTTA be one in there somewhere if so
topSharedWordsFound = model.most_similar(wordSplit, topn=40)
# TODO: Stay DRY! Functionalize the list comp with a second num param
topSharedWords = [
    topWord for topWord in topSharedWordsFound if topWord[1] > .49]

# Just in case
if len(topSharedWordsFound) == 0:
    print("Didn't find any words that had a >.49 distance, so here's some more. (But they probably REALLY suck!)")
    topShared = [
        topWord for topWord in topSharedWordsFound if topWord[1] > .21]

# Print all the top words we have just found
print("=+ The closer the 1.0 the number is, the more similar they are! +=")
for i, topWord in enumerate(topSharedWords):
    print(
        f"The #{i+1} word to use is '{topWord[0]}' with a distance of {topWord[1]}")
    currWord = topWord[0]
    """
    Go ahead and check out each individual distances, if you so choose.
    I was thinking maybe have a boolean to show someone more stats, but eh. If this all turns into routes, it'll be a diff route entirely.
    """
    # for givenWord in wordSplit:
    #     print(
    #         f"The distance between {givenWord} and {currWord} is {model.similarity(givenWord, currWord)}")

# TODO: Give the option to get top words for every 4-word permutation there is, shown in a more concise way
#       This is for later though, let's first functionalize everything into a utils folder or whatever
#       Add in accounting for other words in the list (there looks to be a way you can give negative words for the most_similar function)
#       And make everything routes and such, if functions aren't already enough at least, because one long script is meh
