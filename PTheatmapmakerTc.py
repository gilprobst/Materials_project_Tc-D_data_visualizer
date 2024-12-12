from pymatgen.core import Composition
from pymatgen.util import plotting
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

Tcavg=[]
Tc5=[]
Tcavgatomwv=[]
Tcavgweightwv=[]
Tcavgex0=[]
Tc5ex0=[]
Tcavgatomwvex0=[]
Tcavgweightwvex0=[]
E=[]    
    
f = open("elementslist","r")

lines = f.readlines()

for line in lines:
	line=line.strip(" \n")
	E.append(line)

f.close()
	
g = open("TcValuesavg","r") #list of avg Tc values for each element

lines = g.readlines()

for line in lines:
	if line == '\n':
		Tcavg.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavg.append(float(line))	
g.close()

h = open("TcValuesavgatomwv","r") #list of avg Tc values for each element

lines = h.readlines()

for line in lines:
	if line == '\n':
		Tcavgatomwv.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavgatomwv.append(float(line))

h.close()

k = open("TcValuesavgweightwv","r") #list of avg Tc values for each element

lines = k.readlines()

for line in lines:
	if line == '\n':
		Tcavgweightwv.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavgweightwv.append(float(line))		
			
k.close()   

l = open("TcValuesavg5","r") #list of avg Tc values for each element

lines = l.readlines()

for line in lines:
	if line == '\n':
		Tc5.append(float(0))
	else:	
		line=line.strip(" \n")
		Tc5.append(float(line))		
			
l.close()  

g1 = open("TcValuesavgex0","r") #list of avg Tc values for each element

lines = g1.readlines()

for line in lines:
	if line == '\n':
		Tcavgex0.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavgex0.append(float(line))	
g1.close()

h1 = open("TcValuesavgatomwvex0","r") #list of avg Tc values for each element

lines = h1.readlines()

for line in lines:
	if line == '\n':
		Tcavgatomwvex0.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavgatomwvex0.append(float(line))

h1.close()

k1 = open("TcValuesavgweightwvex0","r") #list of avg Tc values for each element

lines = k1.readlines()

for line in lines:
	if line == '\n':
		Tcavgweightwvex0.append(float(0))
	else:	
		line=line.strip(" \n")
		Tcavgweightwvex0.append(float(line))		
			
k1.close()   

l1 = open("TcValuesavg5ex0","r") #list of avg Tc values for each element

lines = l1.readlines()

for line in lines:
	if line == '\n':
		Tc5ex0.append(float(0))
	else:	
		line=line.strip(" \n")
		Tc5ex0.append(float(line))		
			
l1.close()  
    
elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavg[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-avg")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tc5[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-above5")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavgatomwv[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-atomwv")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavgweightwv[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-weightwv")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavgex0[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-avg-ex0")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tc5ex0[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-above5-ex0")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavgatomwvex0[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-atomwv-ex0")

elemental_Tcata={}
c=0

for i in E:
	elemental_Tcata[i]=Tcavgweightwvex0[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_Tcata, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-Tc-weightwv-ex0")
