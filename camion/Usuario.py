from BusClass import *
#from main import *
lista = []
class usuario:

    def __init__(self,name,lastName,curp):
        self.name=name
        self.lastName=lastName
        self.curp=curp

    def fullName(self):
        return '{} {}'.format(self.name,self.lastName)

    def Agregar(self):
        lista.append(self)
        c.nSeats-=1
        print(f'agregado {self.fullName()}')
        print(f'quedan {c.nSeats} asientos')
        print(f'esta lleno: {c.isFull()}')

    def bajar(self):
        lista.remove(self)
        c.nSeats += 1
        print(f'se ha bajado {self.fullName()}')
        print(f'quedan {c.nSeats} asientos')
        print(f'esta lleno: {c.isFull()}')

i=0
ent=int(input('cuantos usuarios suben?'))
while(i<ent):
    x = input("nombre: ")
    y = input("apellido: ")
    z = input("curp: ")
    u = usuario(x, y, z)
    u.Agregar()
    i += 1

u.bajar()
