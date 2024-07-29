import random
from breezypythongui import EasyFrame
from tkinter.font import Font

class Diceroll(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Roll Dice")

        self.setBackground("lavender")

        self.l = self.addLabel(text="Click roll dice to proceed the GAME!!!", row=0, column=0, background="lavender")
        self.l1 = self.addLabel(text="", row=2, column=1, background="lavender")
        self.b1 = self.addButton(text="Roll Dice", row=1, column=0, command=self.roll_dice)

        # Initialize font
        self.font = Font(family="Verdana", size=100, slant="italic")
        self.l1["font"] = self.font
        self.l1["foreground"] = "black"
        
        # Placeholder for result label
        self.result_label = self.addLabel(text="", row=1, column=1, font=("Autumn"), background="lavender")

    def roll_dice(self):
        # Dice faces
        value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        result = random.choice(value)
        self.l1["text"] = result
        
        # Update result label text based on dice roll
        if result == '\u2680':
            self.result_label["text"] = "You rolled a one! Click roll dice to roll again."
        elif result == '\u2681':
            self.result_label["text"] = "You rolled a two! Click roll dice to roll again."
        elif result == '\u2682':
            self.result_label["text"] = "You rolled a three! Click roll dice to roll again."
        elif result == '\u2683':
            self.result_label["text"] = "You rolled a four! Click roll dice to roll again."
        elif result == '\u2684':
            self.result_label["text"] = "You rolled a five! Click roll dice to roll again."
        elif result == '\u2685':
            self.result_label["text"] = "You rolled a six! Click roll dice to roll again."

def main():
    Diceroll().mainloop()

if __name__ == "__main__":
    main()
