#!/usr/bin/env python
# MouseTrap.py
# by John Shaffstall

import Tkinter
import numpy

class MouseTrap:
    # Public Methods

    # constructor
    def __init__(self):
        self.canvasColor = "black"
        self.lineColor = "red"
        self.pointColor = "white"

        # Tk window
        self.window = Tkinter.Tk()
        self.window.title("MouseTrap")
        self.window.resizable(0, 0)

        # window key bindings
        self.window.bind('<Key-Return>', self._onReturn)

        # Tk canvas widget
        self.canvas = Tkinter.Canvas(self.window, bg=self.canvasColor, width=640, height= 640)
        self.canvas.configure(cursor="crosshair")
        self.canvas.pack()

        # canvas mouse bindings
        self.canvas.bind("<Button-1>", self._onMouseDown)
        self.canvas.bind("<Motion>", self._onMouseMove)
        self.canvas.bind("<ButtonRelease-1>", self._onMouseUp)

        # canvas mouse tracker
        self.positions = []
        self.mouseIsDown = False

    # opens a Tk window for mouse capture
    def open(self):
        self._reset()
        self.window.mainloop()

    def getPositions(self):
        return list(self.positions)

    # returns a 2D numpy array
    # axis = 0 for grouping by dimensions
    # axis = 1 for grouping by pair
    def getNumpyPositions(self, axis=0):
        axisDimensions = 0
        axisPairs = 1
        numpyPositions = numpy.concatenate(self.positions, axis=axis)
        numpyPositions.resize((len(self.positions), 2))
        if (axis == axisDimensions):
            numpyPositions = numpyPositions.transpose()
        return numpyPositions

    # print the current positions to the console
    def printPositions(self):
        print "MouseTrap positions: count = %i" %(len(self.positions))
        print self.positions

    # Private Methods

    def addPosition(self, position):
        if len(position) == 2:
            self.positions.append(position)

            x = position[0]
            y = position[1]
            # self.canvas.create_line(self.getPositions(), fill=self.lineColor)
            self.canvas.create_oval(x, y, x+2, y+2, fill=self.pointColor)

    def _getEventPosition(self, event):
        position = numpy.array([event.x, event.y])
        return position

    # key bindings
    def _onReturn(self, event):
        self.close()

    # mouse bindings
    def _onMouseDown(self, event):
        self.mouseIsDown = True;
        position = self._getEventPosition(event)
        self.addPosition(position)

    def _onMouseMove(self, event):
        if self.mouseIsDown:
            position = self._getEventPosition(event)
            self.addPosition(position)

    def _onMouseUp(self, event):
        self.mouseIsDown = False

    def close(self):
        self.window.quit()

    def _reset(self):
        # remove all mouse positions from the array
        del self.positions[:]


if __name__ == "__main__":
    mouseTrap = MouseTrap()
    mouseTrap.open()

    positions = mouseTrap.getPositions()
    print "positions"
    print positions

    positions0 = mouseTrap.getNumpyPositions(axis=0)
    print "axis=0"
    print positions0

    positions1 = mouseTrap.getNumpyPositions(axis=1)
    print "axis=1"
    print positions1
