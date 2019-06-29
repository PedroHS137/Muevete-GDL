#from Usuario import *

class BusClass:

    def __init__(self,nSeats,route):
        self.nSeats=nSeats
        self.route=route

    def isFull(self):
        if self.nSeats<=0:
            return True
        else:
            return False

c = BusClass(20, 380)  #numero de asientos del camion asi como la ruta





