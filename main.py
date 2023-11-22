from spell_corrector import SpellCorrector


def main():
    spell_corrector = SpellCorrector()
    while True:
        word_to_correct = input("Enter word >")
        matches = spell_corrector.correction(word_to_correct)
        print_results(matches)

def print_results(matches):
    for word in matches:
        print(word)

if __name__ == '__main__':
    main()
