import re
import os
from collections import Counter
#from fuzzywuzzy import process

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class WordHelper:

  @staticmethod
  def words(text):
    return re.findall(r'\w+', text.lower())


class SpellCorrector:
  WORDS = Counter(WordHelper.words(open(os.path.join(__location__,'data/big.txt')).read()))
  WORDS_SET = set(WordHelper.words(open(os.path.join(__location__,'data/big.txt')).read()))

  def P(self, word, N=sum(WORDS.values())):
    "Probability of `word`."
    return SpellCorrector.WORDS[word] / N

  def correction(self, word, num_corrections=1):
    "Most probable spelling correction(s) for word. Number of corrections can be specified."
    sorted_candidates = sorted(self.candidates(word), key=self.P, reverse=True)
    return sorted_candidates[:num_corrections]

  def candidates(self, word):
    "Generate possible spelling corrections for word."
    #return self.known_fuzzy(word)
    return (
      self.known([word]) or
      self.known(self.edits1(word)) or
      self.known(self.edits2(word)) or
      [word]
      )

  def known(self, words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in SpellCorrector.WORDS)

  def known_fuzzy(self, word):
    best_matches = [a[0] for a in process.extractBests(word, SpellCorrector.WORDS_SET)]
    return set(a for a in best_matches if a in SpellCorrector.WORDS)

  def edits1(self, word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

  def edits2(self, word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))
