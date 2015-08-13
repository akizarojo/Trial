# -*- coding: utf-8 -*-

def cleanse(sentence):
    if '"' in sentence and sentence.count('"') % 2 != 0:
      if '" ' in sentence or sentence[-1] == '"':
        sentence = '"%s' % sentence
      else:
        sentence = '%s"' % sentence
    elif '”' in sentence and '“' not in sentence:
      sentence = '“%s' % sentence
    elif '“' in sentence and '”' not in sentence:
      sentence = '%s”' % sentence

    return sentence

print cleanse("""A personal grudge prompted Catapan to attack the couple using a sword," he said.""")