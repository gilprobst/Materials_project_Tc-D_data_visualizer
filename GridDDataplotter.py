from pymatgen.core import Composition
from pymatgen.util import plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import numpy as np

E=[] #list of elements

Dboth=[]
Dboth1=[]
	    
f = open("elementslist","r")

lines = f.readlines()

for line in lines:
	line=line.strip(" \n")
	E.append(line)

f.close()

z = open("2ElementsDdata","r")

lines = z.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)):
		Dboth1.append(float(L[i]))	
	Dboth.append(Dboth1)
	Dboth1=[]
z.close()

data = np.array(Dboth)

Elements1=E
Elements2=E
	
fig, ax = plt.subplots(figsize=(16,12))
im = ax.imshow(data)

ax.set_xticks(np.arange(0,92,1))
ax.set_yticks(np.arange(0,92,1)) 
ax.set_xticklabels(Elements1)
ax.set_yticklabels(Elements2)


ax.set_title("Elements")

fig.colorbar(im, ax=ax, label='DValue')

fig.tight_layout()

plt.savefig("2ElementsDGrid")	

plt.show()
