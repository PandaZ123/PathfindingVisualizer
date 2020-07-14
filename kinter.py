import tkinter as tk
import search
import pygame


class App(tk.Tk):
    end_coord = ['', '']
    start_coord = ['', '']
    randomize = False
    start_algo = False
    start_coord_changed = False
    end_coord_changed = False

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("200x200")
        self.start_label = tk.Label(self, text="Start Coord:")
        self.start_label.place(relx=0.2, rely=0.2, anchor="center")
        self.start_entry_x = tk.Entry(self, width=3)
        self.start_entry_x.insert(0, "")
        self.start_entry_x.place(relx=0.45, rely=0.2, anchor="center")
        self.start_entry_y = tk.Entry(self, width=3)
        self.start_entry_y.insert(0, "")
        self.start_entry_y.place(relx=0.6, rely=0.2, anchor="center")
        self.start_button = tk.Button(self, text="Change",
                                      command=self.on_start_button, width=6)
        self.start_button.place(relx=0.8, rely=0.2, anchor="center")

        self.end_label = tk.Label(self, text="End Coord:")
        self.end_label.place(relx=0.2, rely=0.4, anchor="center")
        self.end_entry_x = tk.Entry(self, width=3)
        self.end_entry_x.insert(0, "")
        self.end_entry_x.place(relx=0.45, rely=0.4, anchor="center")
        self.end_entry_y = tk.Entry(self, width=3)
        self.end_entry_y.insert(0, "")
        self.end_entry_y.place(relx=0.6, rely=0.4, anchor="center")
        self.end_button = tk.Button(self, text="Change",
                                    command=self.on_end_button, width=6)
        self.end_button.place(relx=0.8, rely=0.4, anchor="center")

        self.lbl_x = tk.Label(self, text="x")
        self.lbl_x.place(relx=0.45, rely=0.08, anchor="center")
        self.lbl_y = tk.Label(self, text="y")
        self.lbl_y.place(relx=0.6, rely=0.08, anchor="center")

        self.lbl_random = tk.Label(self, text="Randomize Walls:")
        self.lbl_random.place(relx=0.3, rely=0.6, anchor="center")
        self.random_button = tk.Button(self, text="Randomize",
                                       command=self.on_random_button, width=8)
        self.random_button.place(relx=0.8, rely=0.6, anchor="center")

        self.algo_button = tk.Button(self, text="Start Search",
                                     command=self.on_algo_button, width=10)
        self.algo_button.place(relx=0.5, rely=0.8, anchor="center")

    def on_start_button(self):
        self.start_coord = [self.start_entry_x.get(), self.start_entry_y.get()]
        self.start_coord_changed = True

    def on_end_button(self):
        self.end_coord = [self.end_entry_x.get(), self.end_entry_y.get()]
        self.end_coord_changed = True

    def on_random_button(self):
        self.randomize = True

    def on_algo_button(self):
        self.start_algo = True
        self.destroy()
        self.quit()


if __name__ == '__main__':
    app = App()
    app.mainloop()
    print(app.end_coord)

