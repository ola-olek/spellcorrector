import tkinter

from spell_corrector import SpellCorrector, SpellCorrectorGUI


def main():
    spell_corrector = SpellCorrector()
    root = tkinter.Tk()
    SpellCorrectorGUI(spell_corrector, root)
    root.mainloop()

def print_results(matches):
    for word in matches:
        print(word)

if __name__ == '__main__':
    main()
