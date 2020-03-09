# coding:utf-8
import sys

import nltk
from nltk.corpus import brown

genre_word = [(genre, word)
              for genre in brown.categories()
              for word in brown.words(categories=genre)]

cfd = nltk.ConditionalFreqDist(genre_word)

cfd.plot(
  conditions = ['news', 'adventure'],
  samples = [u'stock', 
                u'sunbonnet', 
                u'Elevated', 
                u'narcotic', 
                u'four', 
                u'woods', 
                u'railing', 
                u'Until', 
                u'aggression', 
                u'marching', 
                u'looking', 
                u'eligible', 
                u'electricity', 
                u'$25-a-plate', 
                u'consulate', 
                u'Casey', 
                u'all-county', 
                u'Belgians', 
                u'Western', 
                u'1959-60', 
                u'Duhagon', 
                u'sinking', 
                u'1,119', 
                u'co-operation', 
                u'Famed', 
                u'regional', 
                u'Charitable', 
                u'appropriation', 
                u'yellow', 
                u'uncertain', 
                u'Heights', 
                u'bringing', 
                u'prize', 
                u'Loen', 
                u'Publique', 
                u'wooden', 
                u'Loeb', u'963', 
                u'specialties', 
                u'Sands', 
                u'succession', 
                u'Paul', 
                u'Phyfe'
              ])

def generate_model(cfdist, word, num=10):
  for i in range(num):
    print(word)
    word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')

bigrams = nltk.bigrams(text)

cfd = nltk.ConditionalFreqDist(bigrams)
generate_model(cfd, 'the')