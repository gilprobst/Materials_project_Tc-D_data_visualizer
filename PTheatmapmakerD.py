from pymatgen.core import Composition
from pymatgen.util import plotting
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

Davg=[]
Davgatomwv=[]
Davgweightwv=[]
E=[]    
    
f = open("elementslist","r")

lines = f.readlines()

for line in lines:
	line=line.strip(" \n")
	E.append(line)

f.close()
	
g = open("DValuesavg","r") #list of avg D values for each element

lines = g.readlines()

for line in lines:
	if line == '\n':
		Davg.append(float(0))
	else:	
		line=line.strip(" \n")
		Davg.append(float(line))	
g.close()

h = open("DValuesavgatomwv","r") #list of avg D values for each element

lines = h.readlines()

for line in lines:
	if line == '\n':
		Davgatomwv.append(float(0))
	else:	
		line=line.strip(" \n")
		Davgatomwv.append(float(line))

h.close()

k = open("DValuesavgweightwv","r") #list of avg D values for each element

lines = k.readlines()

for line in lines:
	if line == '\n':
		Davgweightwv.append(float(0))
	else:	
		line=line.strip(" \n")
		Davgweightwv.append(float(line))		
			
k.close()    
    
elemental_data={}
c=0

for i in E:
	elemental_data[i]=Davg[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_data, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-D-avg")

elemental_data={}
c=0

for i in E:
	elemental_data[i]=Davgatomwv[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_data, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-D-atomwv")

elemental_data={}
c=0

for i in E:
	elemental_data[i]=Davgweightwv[c]
	c=c+1

plotting.periodic_table_heatmap(elemental_data, cbar_label='', cbar_label_size=14, show_plot=False, cmap='GnBu', cmap_range=None, blank_color='grey', edge_color='white', value_format=None, value_fontsize=10, symbol_fontsize=14, max_row=9, readable_fontcolor=True).savefig("PT-D-weightwv")
