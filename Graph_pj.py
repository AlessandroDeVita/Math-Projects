import numpy as np
import matplotlib.pyplot as plt

# make data
x = np.linspace(-10, 10, 100) #setta il dominio + lo spazio fra i punti del dominio
y = 4 + (2 * np.sin(2 * x))/np.cos(x) #riporta la funzione

# plot
fig, ax = plt.subplots() 

ax.plot(x, y, linewidth=2.0) 

ax.set(xlim=(-10, 10), xticks=np.arange(-10, 10),
       ylim=(-10, 10), yticks=np.arange(-10, 10)) #stabilisci la lunghezza degli assi e le etichette dei numeri

plt.show()

