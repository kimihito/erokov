#!/usr/bin/env python
# coding: utf-8
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    
    return m

if __name__ == "__main__":
    filename = "title_sort_uniq2.txt"
    wordlist = []
    src = open(filename,"r").read().split("\n")
    for tmpsrc in src:
        print tmpsrc
        wordlist += wakati(tmpsrc)
        print wordlist
#    erokov = {}
#    w1 = ""
#    w2 = ""
#    for word in wordlist:
#        if w1 and w2:
#            if(w1,w2) not in erokov:
#                erokov[(w1,w2)] = []
#            erokov[(w1,w2)].append(word)
#        w1,w2 = w2, word
#       
#    count = 0
#    sentence = ""
#    w1,w2 = random.choice(erokov.keys())
#    while count < len(wordlist):
#        tmp = random.choice(erokov[(w1,w2)])
#        sentence += tmp
#        w1,w2 = w2, tmp
#        count += 1
#
#
#    print sentence
