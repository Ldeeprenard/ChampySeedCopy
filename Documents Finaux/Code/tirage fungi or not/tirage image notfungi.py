# création d'une visualisation des images en deux catégories, fungi ou non

import pandas as pd
import random

path = r"G:/champybis"


df = pd.read_csv ("FungiNoFungi.csv",index_col=1)
df2 = pd.read_csv ("Champyseed.csv")

tab = df.merge (df2, on= "notreid",how="inner") # Ne garder que les lignes ou fungi_class apparait

tab.path = path+tab.path



#%%
import numpy as np
import matplotlib.pyplot as plt

nombres = np.arange(len(tab[tab["fungi_class"]=="NotFungi"]))  #combien de ligne notfungi

listehasard = random.choices(nombres, k=25) # choisir 25 chiffres aléatoirement parmis le nombre défini ci dessus
j = 1
for i in listehasard:
    filename = tab[tab["fungi_class"]=="NotFungi"].path.iloc[i]

    plt.subplot(5,5,j) # génération des vignettes correspondant aux images notfungi
    img = plt.imread(filename)
    plt.axis('off')
    plt.imshow(img)
    j+=1
plt.axis('off')
plt.show()

#%%
# même chose avec les images dite Fungi

nombres = np.arange(len(tab[tab["fungi_class"]=="Fungi"])) 

listehasard = random.choices(nombres, k=25)
j = 1
for i in listehasard:
    filename = tab[tab["fungi_class"]=="Fungi"].path.iloc[i]

    plt.subplot(5,5,j)
    plt.axis('off')
    img = plt.imread(filename)
    plt.imshow(img)
    j+=1

plt.show()