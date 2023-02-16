# Code Names Word2Vec Guesser

The following program is an implementation of making an application that creates the optimal word for your team in Word 2 Vec.

Guidance from [this article](https://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/) and [this medium post](https://towardsdatascience.com/word2vec-explained-49c52b4ccb71). Using the `GoogleNews-vectors-negative300.bin` dataset at the start, as inspired by [Semantle](https://semantle.com/). It's a bit funky though, so I may look into other datasets out there, especially with better stop words.

The [documentation on gensim](https://radimrehurek.com/gensim/models/word2vec.html) is also very guiding, but mostly I just poke around the source since the documentation is generated from that.

My laptop currently uses 64-bit Python, has 32gb of RAM, and it takes about 48 seconds to load the model the first time- but it saves the gensim model after that. I don't think there's anything else particular relevant for that? I don't think my console can use more than a certain allocation of RAM though.

## Installation

More or less, this is out of the box. You'll want to pip install the following dependencies:
- nltk
- node2vec
- gensim
- numpy
    - May need to do `pip install numpy --upgrade` if you get an error with gensim

For the simulation and analysis stuff:
- matplotlib
- scikit-learn
- pandas

Create a folder called `model` as that is where I save gensim models and where they (probably) should be loaded from.

And then you'll need Google's dataset, which- because it's 1.5gb- is not included in this repository. Download [from Google Drive here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g). You can also use gensim's downloader module to download various datasets and the like, there's a whole bunch of experimentation I guess. I just don't want to train my own model.

## Goal

Just a way to briefly expose myself to finally implementing this kind of thing.

In its most basic form, you input all 25 words on the codenames board. Then you give it the 5 words you need ot make a hint for. And then it spits out a one word (potentially two word? idk) hint given the most related words.

## Notes

TODO: Type up that sheet of paper I have my notes on and slap it into here

To "have fun with it", maybe add in some graphs or analyses or something as well?