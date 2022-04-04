import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def graficar():
    graficaframe = tk.Frame(ventana, height = 400, width = 400)
    graficaframe.place(x = 75, y = 40)
    figura = plt.Figure(figsize=(4, 4), dpi=100)
    lienzo_figura = FigureCanvasTkAgg(figura, graficaframe)
    lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    ax1 = figura.add_subplot()
    ax1.set_title('Top 5 Programming Languages')
    if combograficos.get() == 'barh':
        ax1.barh(list(languages), list(popularity)) #Aqui colocas el tipo de grafico.
        ax1.set_ylabel('Popularity')
        ax1.set_xlabel('Cantidad')
    elif combograficos.get() == 'bar':
        ax1.bar(languages, popularity) #Aqui colocas el tipo de grafico.
        ax1.set_ylabel('Popularity')
        ax1.set_xlabel('Cantidad')
    elif combograficos.get() == 'plot':
        ax1.plot(languages, popularity) #Aqui colocas el tipo de grafico.
        ax1.set_ylabel('Popularity')
        ax1.set_xlabel('Cantidad')
    elif combograficos.get() == 'scatter':
        ax1.scatter(languages, popularity) #Aqui colocas el tipo de grafico.
        ax1.set_ylabel('Popularity')
        ax1.set_xlabel('Cantidad')
    elif combograficos.get() == 'fill_between':
        ax1.fill_between(languages, popularity) #Aqui colocas el tipo de grafico.
        ax1.set_ylabel('Popularity')
        ax1.set_xlabel('Cantidad')
    elif combograficos.get() == 'pie':
        ax1.pie(x = list(popularity), labels = list(languages)) #Aqui colocas el tipo de grafico.
    
    toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
    toolbar.update()
    toolbar.place(x = 100, y = 500)
    

data = {
    'Python': 12,
    'C': 11,
    'Java': 10,
    'C++': 7,
    'C#': 5
}

languages = data.keys()
popularity = data.values()
ventana= tk.Tk()
ventana.geometry('550x550')



tk.Label(ventana, text = 'Bienbenido, elija su estilo de grafica', font = ('Arial', 14, 'bold')).pack()
lista_graficos = ['bar', 'barh', 'plot', 'scatter', 'fill_between', 'pie']
labelopciones = tk.Label(ventana, text = 'Elige un Grafico:', font = ('Arial', 10, 'bold'))
labelopciones.place(x = 75, y = 440)
combograficos = ttk.Combobox(ventana, values = lista_graficos)
combograficos.place(x = 190, y = 440)
botongraficos = ttk.Button(ventana, text = 'Grafica', command = graficar)
botongraficos.place(x = 350, y = 440)


ventana.mainloop()
