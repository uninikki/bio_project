import tkinter as tk
import textwrap
import random, time
from abc import abstractmethod
from tkinter import *
# BioApplication class code from https://www.youtube.com/watch?v=jBUpjijYtCk


class BioApplication(tk.Tk):
    """The main class of the application. Has a container that contains all frames in the application."""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (DNAtoRNA, DNACompliment, RNAtoAminoAcid):
            frame = F(container, self)
            self.frames[F] = frame
            print(self.frames)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(DNAtoRNA)

    def show_frame(self, cont):
        """Displays the frame cont."""
        frame = self.frames[cont]
        frame.tkraise()


class BaseFrame(tk.Frame):
    @abstractmethod
    def button_clicked(self):
        return


class DNAtoRNA(BaseFrame):
    """Class that displays the DNA to RNA Frame."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # labels
        self.title = tk.Label(self, text='DNA -> RNA', font=("Power green", 14))
        self.title.pack(pady=10, padx=10)

        self.label = tk.Label(self, text='Insert template strand here!', font=("Power green", 14))
        self.label.pack()

        # entries
        self.entry = Entry(self, width=100)
        self.entry.pack()

        self.entry_result = Entry(self, width=100, state="disabled")
        self.entry_result.pack()

        # buttons
        self.button = tk.Button(self, text='Convert to RNA', font=("Power green", 12))
        self.button['command'] = self.button_clicked
        self.button.pack()

        self.rna_to_aa = tk.Button(self, text='RNA to amino acid', font=("Power green", 12),
                                   command=lambda: controller.show_frame(RNAtoAminoAcid))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_compliment = tk.Button(self, text='DNA Compliment Finder', font=("Power green", 12),
                                        command=lambda: controller.show_frame(DNACompliment))
        self.dna_compliment.pack(fill=X, expand=TRUE, side=LEFT)

    def button_clicked(self):
        # enable the entry box before anything is done
        self.entry_result.config(state="normal")
        # Clear this textbox before inserting anything else
        self.entry_result.delete(0, "end")
        text = self.entry.get()
        valid_text = is_valid_template(text)

        # Check which button was clicked, and behave accordingly
        if not valid_text:
            self.entry_result.insert(0, "Invalid template entered.")
        else:
            # call a function that converts the template, and insert that into the result entry box
            self.entry_result.insert(0, convert_to_rna(text))
        # disable the resulting text box.
        self.entry_result.config(state="disabled")


class DNACompliment(BaseFrame):
    """Class that displays the DNA Compliment Frame."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # labels
        self.title = tk.Label(self, text='DNA Compliment Finder', font=("Power green", 14))
        self.title.pack(pady=10, padx=10)

        self.label = tk.Label(self, text='Insert DNA strand here!', font=("Power green", 14))
        self.label.pack()

        # entries
        self.entry = Entry(self, width=100)
        self.entry.pack()
        self.entry_result = Entry(self, width=100, state="disabled")
        self.entry_result.pack()

        # buttons
        self.button = tk.Button(self, text='Find compliment', font=("Power green", 12))
        self.button['command'] = self.button_clicked
        self.button.pack()

        self.rna_to_aa = tk.Button(self, text='RNA to Amino Acid', font=("Power green", 12),
                                   command=lambda: controller.show_frame(RNAtoAminoAcid))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_to_rna = tk.Button(self, text='DNA to RNA', font=("Power green", 12),
                                    command=lambda: controller.show_frame(DNAtoRNA))
        self.dna_to_rna.pack(fill=X, expand=TRUE, side=LEFT)

    def button_clicked(self):
        # enable the entry box before anything is done
        self.entry_result.config(state="normal")
        # Clear this textbox before inserting anything else
        self.entry_result.delete(0, "end")
        text = self.entry.get()
        valid_text = is_valid_template(text)

        # Check which button was clicked, and behave accordingly
        if not valid_text:
            self.entry_result.insert(0, "Invalid template entered.")
        else:
            # call a function that converts the template, and insert that into the result entry box
            self.entry_result.insert(0, find_compliment(text))
            # disable the resulting text box.
        self.entry_result.config(state="disabled")


class RNAtoAminoAcid(BaseFrame):
    """Class that displays the RNA to Amino Acid Frame."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # labels
        self.title = tk.Label(self, text='RNA -> Amino Acid', font=("Power green", 14))
        self.title.pack(pady=10, padx=10)

        self.label = tk.Label(self, text='Insert RNA strand here!', font=("Power green", 14))
        self.label.pack()

        # entries
        self.entry = Entry(self, width=100)
        self.entry.pack()

        self.entry_result = Entry(self, width=100, state="disabled")
        self.entry_result.pack()

        # buttons
        self.button = tk.Button(self, text='Convert to Amino acid', font=("Power green", 12))
        self.button['command'] = self.button_clicked
        self.button.pack()

        self.rna_to_aa = tk.Button(self, text='Visualize DNA', font=("Power green", 12),
                                   command=lambda: controller.show_frame(VisualizeDNA))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_compliment = tk.Button(self, text='DNA Compliment Finder', font=("Power green", 12),
                                        command=lambda: controller.show_frame(DNACompliment))
        self.dna_compliment.pack(fill=X, expand=TRUE, side=LEFT)

    def button_clicked(self):
        # enable the entry box before anything is done
        self.entry_result.config(state="normal")
        # Clear this textbox before inserting anything else
        self.entry_result.delete(0, "end")
        text = self.entry.get()
        valid_text = is_valid_rna(text)

        # Check which button was clicked, and behave accordingly
        if not valid_text:
            self.entry_result.insert(0, "Invalid RNA strand entered.")
        else:
            # call functions that divides the rna into triplets, converts to amino acids,
            # and insert that into the result entry box.
            self.entry_result.insert(0, convert_to_aa(divide_rna(text)))
            # divides the original entry into triplets for readability
            self.entry.delete(0, "end")
            self.entry.insert(0, divide_rna(text))
            # disable the resulting text box.
        self.entry_result.config(state="disabled")


# Todo
class VisualizeDNA(BaseFrame):
    """Class that displays the Visualize DNA Frame."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # labels
        self.title = tk.Label(self, text='DNA -> RNA', font=("Power green", 14))
        self.title.pack(pady=10, padx=10)

        self.label = tk.Label(self, text='Insert template strand here!', font=("Power green", 14))
        self.label.pack()

        # entries
        self.entry = Entry(self, width=100)
        self.entry.pack()

        self.entry_result = Entry(self, width=100, state="disabled")
        self.entry_result.pack()

        # buttons
        self.button = tk.Button(self, text='Convert to RNA', font=("Power green", 12))
        self.button['command'] = self.button_clicked
        self.button.pack()

        self.rna_to_aa = tk.Button(self, text='RNA to amino acid', font=("Power green", 12),
                                   command=lambda: controller.show_frame(RNAtoAminoAcid))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_compliment = tk.Button(self, text='DNA Compliment Finder', font=("Power green", 12),
                                        command=lambda: controller.show_frame(DNACompliment))
        self.dna_compliment.pack(fill=X, expand=TRUE, side=LEFT)

    def button_clicked(self):
        # enable the entry box before anything is done
        self.entry_result.config(state="normal")
        # Clear this textbox before inserting anything else
        self.entry_result.delete(0, "end")
        text = self.entry.get()
        valid_text = is_valid_rna(text)

        # Check which button was clicked, and behave accordingly
        if not valid_text:
            self.entry_result.insert(0, "Invalid RNA strand entered.")
        else:
            # call functions that divides the rna into triplets, converts to amino acids,
            # and insert that into the result entry box.
            self.entry_result.insert(0, convert_to_aa(divide_rna(text)))
            # divides the original entry into triplets for readability
            self.entry.delete(0, "end")
            self.entry.insert(0, divide_rna(text))
            # disable the resulting text box.
        self.entry_result.config(state="disabled")


def find_compliment(dna_strand: str) -> str:
    """Given dna_strand, returns it's dna compliment."""
    dna_strand = dna_strand.upper()
    dna_compliment = ""

    for nucleotide in dna_strand:
        if nucleotide == "A":
            dna_compliment += "T"
        elif nucleotide == "C":
            dna_compliment += "G"
        elif nucleotide == "G":
            dna_compliment += "C"
        else:
            dna_compliment += "A"
    return dna_compliment


def is_valid_template(template: str) -> bool:
    """Returns if template is a valid dna strand or not."""
    text = template.upper()
    check = True
    for nucleotide in text:
        if nucleotide.isnumeric() or not nucleotide.isalpha():
            check = False
        elif nucleotide != "A" and nucleotide != "T" and nucleotide != "C" and nucleotide != "G":
            check = False
    return check


def convert_to_rna(template: str) -> str:
    """Converts the given template to rna."""
    template = template.upper()
    rna_compliment = ""

    for nucleotide in template:
        if nucleotide == "A":
            rna_compliment += "U"
        elif nucleotide == "C":
            rna_compliment += "G"
        elif nucleotide == "G":
            rna_compliment += "C"
        else:
            rna_compliment += "A"
    return rna_compliment


def is_valid_rna(rna: str) -> bool:
    """Checks if an rna strand is valid."""
    text = rna.upper()
    check = True
    for nucleotide in text:
        if nucleotide.isnumeric() or not nucleotide.isalpha():
            check = False
        elif nucleotide != "A" and nucleotide != "U" and nucleotide != "C" and nucleotide != "G":
            check = False
    return check


def divide_rna(rna: str) -> str:
    """Given an rna strand, divides it up into pairs of 3.
    >>> divide_rna("AUGGAG")
    'AUG GAG'
    >>> divide_rna("AAGU")
    'AAG U'
    """
    rna = rna.upper()
    wrapper = textwrap.wrap(rna, 3)
    divided = ""
    for triplet in wrapper:
        if wrapper.index(triplet) != 0:
            divided += " " + triplet
        else:
            divided += triplet
    return divided


def convert_to_aa(rna: str) -> str:
    """Given rna, returns the corresponding amino acids as a string. Codons contains the rna sequences associated
    with each amino acid.
    """
    # Add each of the codons (triplets) to a single list
    divided_rna = divide_rna(rna).split(" ")
    aa = ""
    codons = {"Ala": ["GCA", "GCC", "GCG", "GCU"], "Cys": ["UGC", "UGU"], "Asp": ["GAC", "GAU"],
              "Ile": ["AUU", "AUC", "AUA"], "Leu": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
              "Val": ["GUU", "GUC", "GUA", "GUG"], "Phe": ["UUU", 'UUC'], "Met": ["AUG"],
              "Gly": ["GGU", "GGC", "GGA", "GGG"], "Pro": ["CCU", "CCC", "CCA", "CCG"],
              "Thr": ["ACU", "ACC", "ACA", "ACG"], "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
              "Tyr": ["UAU", "UAC"], "Trp": ["UGG"], "Gln": ["CAA", "CAG"], "Asn": ["AAU", "AAC"],
              "His": ["CAU", "CAC"], "Glu": ["GAA", "GAG"], "Lys": ["AAA", "AAG"],
              "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "Stop": ["UAA", "UAG", "UGA"]}

    # Iterate through divided_rna and add the corresponding amino acid to aa
    for triplet in divided_rna:
        for key, value in codons.items():
            if triplet in value and aa == "":
                aa += key
            elif triplet in value and aa != "":
                aa += " " + key
    return aa

# todo
# A modified version of DNA by Al Sweigart al@inventwithpython.com

def dna_animation(template: str, pause: float):
    compliment = find_compliment(template)

    # These are the individual rows of the DNA animation:
    ROWS = [
        # 123456789 <- Use this to measure the number of spaces:
        '         ##',  # Index 0 has no {}.
        '        #{}-{}#',
        '       #{}---{}#',
        '      #{}-----{}#',
        '     #{}------{}#',
        '    #{}------{}#',
        '    #{}-----{}#',
        '     #{}---{}#',
        '     #{}-{}#',
        '      ##',  # Index 9 has no {}.
        '     #{}-{}#',
        '     #{}---{}#',
        '    #{}-----{}#',
        '    #{}------{}#',
        '     #{}------{}#',
        '      #{}-----{}#',
        '       #{}---{}#',
        '        #{}-{}#']
    # 123456789 <- Use this to measure the number of spaces:

    time.sleep(2)
    row_index = 0
    i = 0
    while True:
        # Increment row_index to draw next row:
        row_index = row_index + 1
        if row_index == len(ROWS):
            row_index = 0
        # Row indexes 0 and 9 don't have nucleotides:
        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
        # Select random nucleotide pairs, guanine-cytosine and
        # adenine-thymine:

        left_nucleotide = template[i]
        right_nucleotide = compliment[i]

        # Print the row.
        print(ROWS[row_index].format(left_nucleotide, right_nucleotide))
        i += 1
        time.sleep(pause)  # Add a slight pause.


if __name__ == "__main__":
    app = BioApplication()
    app.mainloop()
