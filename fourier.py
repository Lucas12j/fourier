import matplotlib.pyplot as mat
import numpy as ny
import os

class grafico:

    def show_harm(self, a):
        b = 1
        for i in range (0, a):
            x = ny.arange(-1, 1, 0.01)
            y = ((2 / (b*2*ny.pi)) * (ny.sin(b*2*ny.pi* x))) #Aqui onde se deve escrever a função matemática, considerei T igual a 1 e w0 = 2pi
            mat.plot(x, y)
            mat.title("HARMÔNICO %d" % (i+1))
            mat.show()


    def create_matrix(self, nline):
        matrix = []
        b = 1
        for i in range(0, nline):
            x = ny.arange(-1, 1, 0.01)
            y = ((2 / (b*2*ny.pi)) * (ny.sin(b*2*ny.pi* x)))#Aqui onde se deve escrever a função matemática, considerei T igual a 1 e w0 = 2pi
            matrix.append(y)
            b += 2
        return matrix, len(y)

    def create_array(self, matrix, a, t):
        array=[]
        x=0.0

        for j in range(t):
            for i in range(a):
                x += matrix[i][j]
            array.append(x)
            x=0.0
        return array

    def overlap_harm(self, a):
        b = 1
        for i in range(0, a):
            x = ny.arange(-1, 1, 0.01)
            y = ((2 / (b * 2 * ny.pi)) * (ny.sin(b * 2 * ny.pi * x)))  #Aqui onde se deve escrever a função matemática, considerei T igual a 1 e w0 = 2pi
            b += 2
            mat.plot(x, y)
            mat.title("HARMÔNICOS SOBREPOSTOS")
        mat.show()

    def fourier(self, array):
        x = ny.arange(-1, 1, 0.01)
        mat.plot(x, array)
        mat.title("TRANSFORMADA DE FOURIER")
        mat.show()

print(" \n\n\n                              ***(PLOTAR TRANSFORMADA DE FOURIER)***\n")
g = grafico()
i=10    #Valores de inicialização para não dar conflito com os if's
a=10
while (i != 0 and a != 0):
    a = int(input('\nENTRE COM A QUANTIDADE DE ITERAÇÕES: '))
    i=10
    while (i != 0 and a != 0 and i!=4):
         print("\n=======================================================\n1- MOSTRAR GRÁFICO DE CADA HARMONICO\n2- MOSTRAR OS HARMONICOS SOBREPOSTOS\n3- MOSTRAR O GRÁFICO DA TRANFORMADA CALCULADA\n4- FAZER OUTRA ITERAÇÃO\n0- PARA FECHAR O PROGRAMA.\n=======================================================")
         i = int(input('\nENTRE COM A OPÇÃO DESEJADA '))
         if (i==1 and i != 0 and a != 0):
            g.show_harm(a)
         elif (i==2 and i != 0 and a != 0):
             g.overlap_harm(a)
         elif (i==3 and i != 0 and a != 0):
            matrix, t = g.create_matrix(a)
            array = g.create_array(matrix, a, t)
            g.fourier(array)
         if (os.name == 'nt'):
             os.system("cls")
         else:
             os.system("clear")
print("FIM DO PROGRAMA")