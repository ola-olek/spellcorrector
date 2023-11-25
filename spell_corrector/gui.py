import tkinter as tk
from tkinter import ttk, scrolledtext


class SpellCorrectorGUI:
    def __init__(self, spell_corrector, root):
        self.spell_corrector = spell_corrector
        self.root = root
        self.root.title("Spell Corrector")
        self.root.geometry("350x420")
        self.create_widgets()

    def create_widgets(self):
        self.label_input = tk.Label(self.root, text="Enter a word:").pack()
        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack(pady=5)

        self.label_matches_number = tk.Label(self.root, text="Choose number of matches (default=1):").pack()
        self.selected_value = tk.StringVar()
        self.matches_number_combobox = ttk.Combobox(self.root, values=list(range(1, 11)), textvariable=self.selected_value)
        self.matches_number_combobox.current(0)
        self.matches_number_combobox.pack(pady=5)

        self.label_output = tk.Label(self.root, text="Corrected word(s):").pack()
        self.output = scrolledtext.ScrolledText(self.root, width=30, height=10)
        self.output.pack(pady=5)

        self.correct_button = tk.Button(self.root, text="Make correction", command=self.correct_word).pack(pady=5)
        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_all).pack(pady=5)

    def clear_all(self):
        self.input_entry.delete(0, tk.END)
        self.output.delete(1.0, tk.END)
        self.matches_number_combobox.current(0)

    def correct_word(self):
        if self.input_entry:
            word_to_correct = self.input_entry.get()
            matches = self.spell_corrector.correction(word_to_correct, int(self.selected_value.get()))
            self.output.delete(1.0, tk.END)
            for match in matches:
                self.output.insert(tk.END, match + "\n")