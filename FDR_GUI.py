import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
#import matplotlib.pyplot as plt
from Plane import Plane
from Sensors import SensorFactory
from Buffer import Buffer
from Log import Log, encoder


style.use("ggplot")
LARGE_FONT=("Verdana",12)
SMALL_FONT=("Verdana",10)
AVAILABLE_SENSORS = ['EngineTempSensor','EngineFuelSensor','AltitudeSensor','TimeSensor','PressureSensor']

def NI():
    print("Not implemented yet!")

def enableWidget(state, widget, entryvariable):
        if state == True:
            widget.configure(state='normal')
        else:
            widget.configure(state='disabled')
            entryvariable.set(0)


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

        label1 = tk.Label(self, text="Data Collector", font=LARGE_FONT)
        label1.grid(row=0,columnspan=5)
        #----------------------------------

        #----------------------------------
        label2 = tk.Label(self, text="Please specify the simulation's parameters below:", font=SMALL_FONT)
        label2.grid(row=2, sticky = 'ew', ipadx = 5, ipady = 5, columnspan=5)
        #----------------------------------
        label31 = tk.Label(self, text="Plane initial velocities:", font=SMALL_FONT)
        label31.grid(row=3, column=0,sticky = 'ew', ipadx = 5, ipady = 5, columnspan=2)
        label32 = tk.Label(self, text="Plane active sensors:", font=SMALL_FONT)
        label32.grid(row=3, column=2,sticky = 'ew', ipadx = 5, ipady = 5, columnspan=2)
        #----------------------------------
        label4 = tk.Label(self, text="Vx", font=SMALL_FONT)
        label4.grid(row=4, column=0,sticky = 'w', ipadx = 5, ipady = 5)

        self.Vx = tk.DoubleVar()
        entry4 = tk.Entry(self, bd =5, state='normal', width = 5, textvariable = self.Vx)
        entry4.grid(row=4, column=1, sticky = 'w')
        #----------------------------------
        label5 = tk.Label(self, text="Vy", font=SMALL_FONT)
        label5.grid(row=5, column=0,sticky = 'w', ipadx = 5, ipady = 5)

        self.Vy = tk.DoubleVar()
        entry5 = tk.Entry(self, bd =5, state='normal', width = 5, textvariable = self.Vy)
        entry5.grid(row=5, column=1, sticky = 'w')
        #----------------------------------
        label6 = tk.Label(self, text="Vz", font=SMALL_FONT)
        label6.grid(row=6, column=0,sticky = 'w', ipadx = 5, ipady = 5)

        self.Vz = tk.DoubleVar()
        entry6 = tk.Entry(self, bd =5, state='normal', width = 5, textvariable = self.Vz)
        entry6.grid(row=6, column=1, sticky = 'w')
        #----------------------------------

        label7 = tk.Label(self, text="Name:", font=SMALL_FONT)
        label7.grid(row=7, column=0,sticky = 'w', ipadx = 5, ipady = 5)

        self.planeName = tk.StringVar()
        entry7 = tk.Entry(self, bd =5, state='normal', width = 10, textvariable = self.planeName)
        entry7.grid(row=7, column=1, sticky = 'ew')
        #----------------------------------


        self.EntryVarList = []
        self.EntryWidgList = []
        self.CheckVarList = []
        self.CheckWidgList = []
        self.SensorDict = {}

        r = 4
        for sensor in AVAILABLE_SENSORS:

            EntryVar = tk.IntVar()
            E = tk.Entry(self, bd =5, state='disabled', width = 5, textvariable = EntryVar,)
            E.grid(row=r, column=3, sticky = 'W')
            CheckVar = tk.IntVar()
            C = tk.Checkbutton(self, text = sensor, justify = tk.LEFT, variable = CheckVar,
                 onvalue = 1, offvalue = 0, height=1, width = 15, command = lambda var=CheckVar,e=E,ev=EntryVar:enableWidget(var.get(), e, ev) )
            C.grid(row=r, column=2)
            self.SensorDict[sensor] = EntryVar
            self.EntryVarList.append(EntryVar)
            self.EntryWidgList.append(E)
            self.CheckVarList.append(CheckVar)
            self.CheckWidgList.append(C)

            r += 1

        button1 = tk.Button(self, text="Simulate!",
                            command=lambda dictionary=self.chosenSensors, plane=self.createPlane: GraphPage(dictionary(), plane()))
        button1.grid(row=20, column=0, sticky='ew', columnspan=6)

        button2 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=22, column=1,columnspan = 2)


    def chosenSensors(self):
        dict = {}
        for s in self.SensorDict.keys():
            if self.SensorDict[s].get() > 0:
                dict[s] = self.SensorDict[s].get()
        return dict

    def createPlane(self):
        return Plane(self.Vx.get(), self.Vy.get(),self.Vz.get(),self.planeName)





class AnalyzerPage(tk.Frame):
# TODO importing and plotting data from db using Log class
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

class GraphPage(tk.Tk):
    def __init__(self, sensors, plane, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.sensors = sensors
        self.plane = plane
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Data Collector", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Abort",
                            command=lambda: self.destroy())
        button1.pack()

        f = Figure(figsize=(10,10), dpi=100)
        self.canvas = FigureCanvasTkAgg(f,self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.charts = self.createPlots(f)

        planeName,header,data = self.runSimulation()

        #Log.saveToCSV(planeName.get(),header,data)


    def createPlots(self,figure):

        self.numberOfPlots = 0
        for s in self.sensors.keys():
            if self.sensors[s] > 0:
                self.numberOfPlots +=1
        self.nRows = 2
        self.nColumns = int(self.numberOfPlots / 2) + self.numberOfPlots % self.nRows

        chartsTable = []
        i = 0
        for row in range(self.nRows):
            rowList = []
            for column in range(self.nColumns):
                i += 1
                if i <= self.numberOfPlots:
                    rowList.append(figure.add_subplot(self.nRows*100+self.nColumns*10+i))
            chartsTable.append(rowList)

        return chartsTable

    def getChart(self,number):
        if self.numberOfPlots < 2:
            return self.charts[number]
        else:
            row = int(number/self.nColumns)
            column = number - row*self.nColumns
            return self.charts[row][column]

    def runSimulation(self):

        sensors = self.sensors
        sensorsList = SensorFactory.createSensorList(sensors, self.plane)
        header = encoder(sensorsList)
        buffer = Buffer(5,sensorsList)
        self.plane.takeoff()                                     # start the simulation

        while self.plane.isFlying() :

            self.plane.update()
            buffer.readData()
            data = buffer.returnDataHorizontal()

            n = 0
            k = 0
            for s in self.sensors.keys():

                self.getChart(n).clear()
                self.getChart(n).set_title(s)
                for i in range(self.sensors[s]):
                    self.getChart(n).plot(data[i+k])

                k += self.sensors[s]

                n += 1
            self.canvas.show()

        return self.plane.getName(),header,buffer.returnDataCopy()
