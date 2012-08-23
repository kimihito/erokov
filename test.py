#!/usr/bin/env python
# coding: utf-8
import MeCab
import nltk

def extractKeyword(text):
    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(text)
    keywords = []
    while node:
        keywords.append(node.feature.split(",")[0])
        node = node.next
    return keywords

if __name__ == "__main__":
    filename = 'title_sort_uniq.txt'
    src = open(filename,'r').read().split("\n")
    word = []
    for tmp in src:
        word += extractKeyword(tmp)
    print len(word)
#    for w in keywords:
#        word.append(w)
#    title =  len(word) / len(src)
#    a = nltk.FreqDist(word)
#    dict(a)
#    print a
