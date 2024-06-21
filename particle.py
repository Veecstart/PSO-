import random

class Particle:
    # Defino as caracteristicas gerais da minha particula
    def __init__(self,n_dimensions,w=0.8,c1=1,c2=1):
        #
        n_dimensions = len()
        #Propiedades do Indivíduo Local
        self.position_local = []
        self.velocity_local = []
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.err_local = -1
        #Ṕropriedade do Indivíduo Global
        self.position_global = []
        self.err_global = -1
        
        #Inicializo a Posição e a Velocidade de cada Particula
        for p in range(0,n_dimensions):
            self.velocity_local.append(random.uniform(-1,1))
            self.position_local.append(function[p])

    #Avalio o fitness particula a particula
    def avaluate():
        pass
    #Atualizo a velocidade da minha particula
    def velocity_update():
        pass
    #Atualizo a posição da minha particula
    def position_update():
        pass

print(Particle([5,5]))