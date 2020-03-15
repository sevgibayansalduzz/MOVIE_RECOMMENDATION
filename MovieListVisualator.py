import tkinter as tk
from tkinter import *

class MovieListVisualator(tk.Frame):
    def __init__(self, root,books):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="LIGHTBLUE")
        self.canvas.bind("<Configure>", self.onCanvasConfigure)
        self.frame = tk.Frame(self.canvas, background="LIGHTBLUE")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.pop(books)

    def onCanvasConfigure(self, event):
        # width is tweaked to account for window borders
        width = event.width - 4
        self.canvas.itemconfigure("self.frame", width=width)

    def pop(self,books):
        backgroundlist = ["WHITE", "LIGHTGREY"]
        for i in range(len(books)):
            self.f = Label(self.frame, text=str(i+1)+")  "+books[i],background=backgroundlist[i%2], height=2, border=1,anchor="w")
            self.f.pack(side="top", fill="both")

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


"""if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("800x500")
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()"""