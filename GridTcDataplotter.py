from pymatgen.core import Composition
from pymatgen.util import plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import numpy as np

E=[] #list of elements

Tcboth=[]
Tcboth1=[]
Tcboth5=[]
Tcex0=[]
	    
f = open("elementslist","r")

lines = f.readlines()

for line in lines:
	line=line.strip(" \n")
	E.append(line)

f.close()

z = open("2ElementsTcdata","r")

lines = z.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)):
		Tcboth1.append(float(L[i]))	
	Tcboth.append(Tcboth1)
	Tcboth1=[]
z.close()

z5 = open("2ElementsTcdata5+","r")

lines = z5.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)):
		Tcboth1.append(float(L[i]))	
	Tcboth5.append(Tcboth1)
	Tcboth1=[]
z5.close()

z0 = open("2ElementsTcdataex0","r")

lines = z0.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)):
		Tcboth1.append(float(L[i]))	
	Tcex0.append(Tcboth1)
	Tcboth1=[]
z0.close()
###########################################
data = np.array(Tcboth)

Elements1=E
Elements2=E
	
fig, ax = plt.subplots(figsize=(16,12))
im = ax.imshow(data)

ax.set_xticks(np.arange(0,92,1))
ax.set_yticks(np.arange(0,92,1))
ax.set_xticklabels(Elements1)
ax.set_yticklabels(Elements2)

ax.set_title("Elements")

fig.colorbar(im, ax=ax, label='TcValue')

fig.tight_layout()

plt.savefig("2ElementsTcGrid")

plt.close()
#######################################
data = np.array(Tcboth5)

Elements1=E
Elements2=E
	
fig, ax = plt.subplots(figsize=(16,12))
im = ax.imshow(data)

ax.set_xticks(np.arange(0,92,1))
ax.set_yticks(np.arange(0,92,1))
ax.set_xticklabels(Elements1)
ax.set_yticklabels(Elements2)

ax.set_title("Elements")

fig.colorbar(im, ax=ax, label='TcValue')

fig.tight_layout()

plt.savefig("2ElementsTc5+Grid")

plt.close()
######################################
data = np.array(Tcex0)

Elements1=E
Elements2=E
	
fig, ax = plt.subplots(figsize=(16,12))
im = ax.imshow(data)

ax.set_xticks(np.arange(0,92,1))
ax.set_yticks(np.arange(0,92,1))
ax.set_xticklabels(Elements1)
ax.set_yticklabels(Elements2)

ax.set_title("Elements")

fig.colorbar(im, ax=ax, label='TcValue')

fig.tight_layout()

plt.savefig("2ElementsTcex0Grid")

plt.close()
