import Tkinter as tk

LARGE_FONT=("Verdana",12)

def NI():
    print("Not implemented yet!")

def qf(param):
    print(param)


class FDR_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CollectorPage, AnalyzerPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Collect Data",
                            command=lambda: controller.show_frame(CollectorPage))
        button1.pack()

        button2 = tk.Button(self, text="Analyze Data",
                            command=lambda: controller.show_frame(AnalyzerPage))
        button2.pack()

        button3 = tk.Button(self, text="Quit",
                            command=lambda: self.quit() )
        button3.pack()


class CollectorPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Data Collector", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="STH", command= lambda : NI())

        button2.pack()

        button1 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class AnalyzerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Data Analyzer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="STH",
                            command=lambda: NI())
        button2.pack()

        button1 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = FDR_GUI()
app.mainloop()
