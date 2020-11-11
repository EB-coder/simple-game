from tkinter import *
import random as rdm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Rock", font=("Times New Roman", 15),
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Scissors", font=("Times New Roman", 15),
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Paper", font=("Times New Roman", 15),
                      command=lambda x=3: self.btn_click(x))
        btn4 = Button(root, text='help with choise',
                      font=('Times New Roman', 11), foreground='green',
                      command=lambda x=4: self.btn_click(x))
        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)
        btn4.place(x=400, y=35, width=120, height=50)

        self.lbl = Label(root, text="Srart the game!", bg="lightyellow2",
                         font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left",
                          font=("Times New Roman", 13, "bold"),
                          text=f"Wins: {self.win} \n Loses:"
                          f" {self.lose} \n Drows: {self.drow}",
                          bg="lightyellow2", fg='blue')
        self.lbl2.place(x=5, y=5)

        self.lbl4 = Label(root, text="random number!", bg="lightyellow2",
                          font=("Times New Roman", 15, "bold"), fg='black')
        self.lbl4.place(x=400, y=5)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)
        any_num = rdm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Drow", fg='violet')
        elif choise == 4:
            self.lbl4.configure(text=str(any_num))

        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Win", fg='green')
        else:
            self.lose += 1
            self.lbl.configure(text="Lose", fg='red')

        self.lbl2.configure(text=f"Wins: {self.win}\nLoses:"
                            f" {self.lose}\nDrows: {self.drow}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("580x200+200+200")
    root.title("rock, scissors, paper")
    root.resizable(False, False)
    root["bg"] = "lightyellow2"
    app = Main(root)
    app.pack()

    root.mainloop()
