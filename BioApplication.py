import tkinter as tk
from tkinter import *
# BioApplication class code from https://www.youtube.com/watch?v=jBUpjijYtCk


class BioApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (DNAtoRNA, DNACompliment):
            frame = F(container, self)
            self.frames[F] = frame
            print(self.frames)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(DNAtoRNA)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class DNAtoRNA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Root window
        # self.title("DNA -> RNA")
        # self.geometry("500x200")

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
                                   command=lambda : controller.show_frame(RNAtoAminoAcid))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_compliment = tk.Button(self, text='DNA Compliment Finder', font=("Power green", 12),
                                        command=lambda : controller.show_frame(DNACompliment))
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


class DNACompliment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label
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

        self.rna_to_aa = tk.Button(self, text='RNA to Amino Acid', font=("Power green", 12))
        self.rna_to_aa.pack(fill=X, expand=TRUE, side=LEFT)

        self.dna_to_rna = tk.Button(self, text='DNA to RNA', font=("Power green", 12),
                                    command=lambda : controller.show_frame(DNAtoRNA))
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


# TODO
class RNAtoAminoAcid(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


# Todo
class VisualizeDNA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


# TODO
class VisualizeRNA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


def find_compliment(dna_strand: str) -> str:
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
    text = template.upper()
    check = True
    for nucleotide in text:
        if nucleotide.isnumeric() or not nucleotide.isalpha():
            check = False
        elif nucleotide != "A" and nucleotide != "T" and nucleotide != "C" and nucleotide != "G":
            check = False
    return check


def convert_to_rna(template: str) -> str:
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


if __name__ == "__main__":
    app = BioApplication()
    app.mainloop()