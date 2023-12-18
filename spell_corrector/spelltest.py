from matplotlib import pyplot as plt

from spell import SpellCorrector


class Spelltest:
    def __init__(self):
        """Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."""
        self.spell_set = [(right, wrong) for (right, wrongs) in (line.split(':')
                          for line in open('data/testset.txt'))
                          for wrong in wrongs.split()]

    def spelltest(self):
        """Run correction(wrong) on all (right, wrong) pairs; report results."""
        n = len(self.spell_set)
        sc = SpellCorrector()

        x_values, y_values = [], []
        for i in range(1, 11):
            good = 0
            for right, wrong in self.spell_set:
                corrections = sc.correction(wrong, num_corrections=i)
                good += (right in corrections)
            print('{:.0%} of {} correct for num_correction={}'.format(good / n, n, i))
            accuracy_percentage = good / n * 100
            x_values.append(i)
            y_values.append(accuracy_percentage)
        self.plot(x_values, y_values)

    def plot(self, x_values, y_values):
        plt.plot(x_values, y_values, marker='o')
        plt.title('Zależność dokladności od maksymalnej liczby oczekiwnaych korekcji')
        plt.xlabel('Max. liczba oczekiwanych korekcji')
        plt.xticks(x_values)
        plt.ylabel('Dokladność [%]')
        plt.show()

if __name__ == '__main__':
    test = Spelltest()
    test.spelltest()