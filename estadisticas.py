from Datos.datos01 import Consulta
from Negocio.negocio import NegocioColsulta
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

class estadisticas():



    def calcEst(self):
        c = NegocioColsulta()


        todos=c.todos()
        for i in todos:
            print(i.id_consulta,'', i.eleccion)

        elecc1= 'hospital'
        elecc2= 'restaurant'
        elecc3= 'supermarket'

        print(c.cant_elecc(elecc1))
        print(c.cant_elecc(elecc2))
        print(c.cant_elecc(elecc3))
        cants=[len(c.cant_elecc(elecc1)), len(c.cant_elecc(elecc2)), len(c.cant_elecc(elecc3))]
        print(cants)

        labels = 'Hospitales', 'Restaurantes', 'Supermercados'
        colors = ['yellowgreen', 'lightcoral', 'lightskyblue']

        plt.title('Porcentaje de consultas por tipo:')
        plt.pie(cants, labels=labels, autopct= '%.1f%%', colors=colors, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
        plt.savefig('static/grafico.png')

        # plt.show()

        plt.clf()

        return True

    def calcHist(self):
        c = NegocioColsulta()
        consultasr = c.histograma('restaurant')
        consultass = c.histograma('supermarket')
        consultash = c.histograma('hospital')

        r =[]
        rh =[]
        s=[]
        sh=[]
        h=[]
        hh=[]

        for i in consultasr:
            r.append(i[0])
            rh.append(i[2])
        for i in consultass:
            s.append(i[0])
            sh.append(i[2])
        for i in consultash:
            h.append(i[0])
            hh.append(i[2])

        plt.title("Restaurants")
        plt.xlabel("Fechas")
        plt.ylabel("Cant consultas")
        plt.plot(r)
        plt.xticks(np.arange(len(rh)), rh)
        plt.savefig('static/rest.png')
        #plt.show()
        plt.clf()


        plt.title("Supermercados")
        plt.xlabel("Fechas")
        plt.ylabel("Cant consultas")
        plt.plot(s)
        plt.xticks(np.arange(len(sh)), sh)
        plt.savefig('static/super.png')
        #plt.show()
        plt.clf()


        plt.title("Hospitales")
        plt.xlabel("Fechas")
        plt.ylabel("Cant consultas")
        plt.plot(h)
        plt.xticks(np.arange(len(hh)), hh)
        plt.savefig('static/hosp.png')
        #plt.show()
        plt.clf()

        return  True

