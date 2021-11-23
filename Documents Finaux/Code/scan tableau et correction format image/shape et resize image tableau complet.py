import pandas as pd
import pathlib
from PIL import Image
import os

df = pd.read_csv ("Champyseed.csv")

path = r"G:/champybis"
df.path = path+df.path


listenb = []
# Parcours de la liste à l'envers pour éviter les problèmes inhérents à la suppression des lignes
for i in range (len(df)-1, -1, -1):
    try:
        print (i)
        imgpath = df["path"].iloc[i]
        image = Image.open(imgpath)
        if image.mode != "RGB": #detecter une image n'ayant pas 3 canaux, ajout à une liste et conversion
            print ("gris",imgpath )
            listenb.append (imgpath)
            image = image.convert("RGB")
            image = image.save (imgpath)
        if image.size != (224,224):   # Si une image n'est pas aux bonnes dimensions
            image = image.resize (224,224)

    except:
        print('Error occur on ' + imgpath) # Si image corrompue, suppression du tableau et du disque dur
        df.drop(i)
        if os.path.exists(imgpath):
             os.remove(imgpath)
        
F = open('list.txt', 'w') 
     
listenb

print (listenb,file=F) #enregistrement de la liste dans un fichier
df.to_csv ("nouveau_tableau")