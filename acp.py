import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('autos_acp.xls')
labels = df.iloc[:,0].values
df = df.iloc[:,1:7]

#préparer le graphique
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(df.CYL,df.PUISS,"o")
ax.axis([1000,3000,50,140])
ax.set_xlabel("CYL")
ax.set_ylabel("PUISS")
#ajouter les labels des véhicules
for v in df.index:
 ax.text(df.CYL[v],df.PUISS[v],labels[v])

#faire afficher
plt.show()