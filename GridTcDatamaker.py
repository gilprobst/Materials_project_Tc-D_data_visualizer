from pymatgen.core import Composition
from pymatgen.util import plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import numpy as np

mat_id=[] #list list of mat_id's
formula=[] #list of the chemical formulas
Tc=[] #list of the SC Tc's
D=[] # ist of the ductability values
C=[] #list of the atomic fractions
E=[] #list of elements
EC=[]
EC1=[]
EC2=[]
EC3=[]
Eboth=[]
Eboth1=[]
Tcboth=[]
Tcboth1=[]
Tclistfive=[]
Tcexzero=[]
N=[]
M=[]
c=0
	    
f = open("elementslist","r")

lines = f.readlines()

for line in lines:
	line=line.strip(" \n")
	E.append(line)

f.close()

g = open("gil.csv","r")

lines = g.readlines()
for i in range(1,len(lines)):
	line=lines[i]
	line=line.strip("\n")
	L=line.split(",")
	mat_id.append(int(L[0]))
	formula.append(L[1])
	Tc.append(float(L[2]))
	D.append(float(L[3]))

for i in formula:
	comp=Composition(i)
	CC=[]
	for j in E:
		CC.append(comp.get_atomic_fraction(j))
	C.append(CC)

g.close()

h = open("Ecomps","r")

lines = h.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)-1):
		EC1.append(str(L[i]))	
	EC.append(EC1)
	EC1=[]

h.close()

k = open("Ecompsindex","r")

lines = k.readlines()

for line in lines:
	line=line.strip(" \n")
	L=line.split(",")
	for i in range(0,len(L)-1):
		EC2.append(int(L[i]))	
	EC3.append(EC2)
	EC2=[]

k.close()

for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Tcboth.append(Tcboth1)
	Tcboth1=[]

for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Tclistfive.append(Tcboth1)
	Tcboth1=[]
	
for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Tcexzero.append(Tcboth1)
	Tcboth1=[]

	
Nl=[]
for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Nl.append(Tcboth1)
	Tcboth1=[]

Ml=[]
for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Ml.append(Tcboth1)
	Tcboth1=[]
Ol=[]
for i in range(len(E)):
	for j in range(len(E)):
		Tcboth1.append(0)
	Ol.append(Tcboth1)
	Tcboth1=[]



for i in range(len(EC3)):
	A=EC3[i]
	for j in range(len(EC3)):
		B=EC3[j]
		N=0
		M=0
		O=0
		for l in A:
			for k in B:
				if l == k:
					N=N+1
					Tcboth[i][j]=float(Tcboth[i][j])+float(Tc[k])
						
					if Tc[k]>5:
						M=M+1
						Tclistfive[i][j]=float(Tclistfive[i][j])+float(Tc[k])
					if float(Tc[k]) != 0:
						O=O+1
						Tcexzero[i][j]=float(Tcexzero[i][j])+float(Tc[k])
			
		if N != 0:
			Tcboth[i][j]=Tcboth[i][j]/N
		if M != 0:
			Tclistfive[i][j]=Tclistfive[i][j]/M
		if O != 0:
			Tcexzero[i][j]=Tcexzero[i][j]/O
		Nl[i][j]=N
		Ml[i][j]=M
		Ol[i][j]=O	
		
z = open("2ElementsTcdata","w")

for i in range(len(Tcboth)):
	for j in range(len(Tcboth[i])):
		if j != len(Tcboth[i])-1:
			z.write(str(Tcboth[i][j])+",")
		else:
			z.write(str(Tcboth[i][j]))
	z.write("\n")
z.close()

z5 = open("2ElementsTcdata5+","w")

for i in range(len(Tclistfive)):
	for j in range(len(Tclistfive[i])):
		if j != len(Tclistfive[i])-1:
			z5.write(str(Tclistfive[i][j])+",")
		else:
			z5.write(str(Tclistfive[i][j]))
	z5.write("\n")
z5.close()

z0 = open("2ElementsTcdataex0","w")

for i in range(len(Tcexzero)):
	for j in range(len(Tcexzero[i])):
		if j != len(Tcexzero[i])-1:
			z0.write(str(Tcexzero[i][j])+",")
		else:
			z0.write(str(Tcexzero[i][j]))
	z0.write("\n")
z0.close()

E2=[]

for i in E:
	dummy=[]
	for j in E:
		dummy.append(str(i)+"-"+str(j))
	E2.append(dummy)

E2vector=[]
for i in range(len(E2)):
	for j in range(len(E2[i])):
		E2vector.append(str(E2[i][j]))
		
Tcbothvector=[]
for i in range(len(Tcboth)):
	for j in range(len(Tcboth[i])):
		Tcbothvector.append(float(Tcboth[i][j]))
		
Tcexzerovector=[]
for i in range(len(Tcexzero)):
	for j in range(len(Tcexzero[i])):
		Tcexzerovector.append(float(Tcexzero[i][j]))
		
Tclistfivevector=[]
for i in range(len(Tclistfive)):
	for j in range(len(Tclistfive[i])):
		Tclistfivevector.append(float(Tclistfive[i][j]))
		
Nlvector=[]
for i in range(len(Nl)):
	for j in range(len(Nl[i])):
		Nlvector.append(str(Nl[i][j]))

Mlvector=[]
for i in range(len(Ml)):
	for j in range(len(Ml[i])):
		Mlvector.append(str(Ml[i][j]))
		
Olvector=[]
for i in range(len(Ol)):
	for j in range(len(Ol[i])):
		Olvector.append(str(Ol[i][j]))	
		
dic={}

dic={"E2":E2vector, "Tc":Tcbothvector, "M":Nlvector}

# Create a list of tuples from the dictionary
tuple_list = list(zip(dic["Tc"], dic["E2"], dic["M"]))

# Sort the list of tuples in descending order based on the values in the "Values" list
sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

# Create three lists from the sorted list of tuples
sorted_Tc, sorted_E2,sorted_M = zip(*sorted_list)

# Update the dictionary with the sorted lists
dic["E2"] = sorted_E2
dic["Tc"] = sorted_Tc
dic["M"] = sorted_M

with open("2Elements_Tc_sorted","w") as n:
	n.write("Combination of Elements,Tc,Nº of Comps"+"\n")
	for i in range(len(dic["E2"])):
		n.write(str(dic["E2"][i])+","+str(dic["Tc"][i])+","+str(dic["M"][i])+"\n")
		
dic={}

dic={"E2":E2vector, "Tc":Tcexzerovector, "M":Olvector}

# Create a list of tuples from the dictionary
tuple_list = list(zip(dic["Tc"], dic["E2"], dic["M"]))

# Sort the list of tuples in descending order based on the values in the "Values" list
sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

# Create three lists from the sorted list of tuples
sorted_Tc, sorted_E2,sorted_M = zip(*sorted_list)

# Update the dictionary with the sorted lists
dic["E2"] = sorted_E2
dic["Tc"] = sorted_Tc
dic["M"] = sorted_M

with open("2Elements_Tcexzero_sorted","w") as n:
	n.write("Combination of Elements,Tc,Nº of Comps"+"\n")
	for i in range(len(dic["E2"])):
		n.write(str(dic["E2"][i])+","+str(dic["Tc"][i])+","+str(dic["M"][i])+"\n")
		
dic={}

dic={"E2":E2vector, "Tc":Tclistfivevector, "M":Mlvector}

# Create a list of tuples from the dictionary
tuple_list = list(zip(dic["Tc"], dic["E2"], dic["M"]))

# Sort the list of tuples in descending order based on the values in the "Values" list
sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

# Create three lists from the sorted list of tuples
sorted_Tc, sorted_E2,sorted_M = zip(*sorted_list)

# Update the dictionary with the sorted lists
dic["E2"] = sorted_E2
dic["Tc"] = sorted_Tc
dic["M"] = sorted_M

with open("2Elements_Tclistfive_sorted","w") as n:
	n.write("Combination of Elements,Tc,Nº of Comps"+"\n")
	for i in range(len(dic["E2"])):
		n.write(str(dic["E2"][i])+","+str(dic["Tc"][i])+","+str(dic["M"][i])+"\n")
		
		
#########################################################################################################################
N=[]
Tc1=[]
with open("TcValues","r") as f:
	lines=f.readlines()
	for line in lines:
		if line == "\n":
			Tc1.append(0)
			N.append(0)
		else:
			line=line.strip("\n")
			L=line.split(",")
			L.pop(-1)
			soma=0
			for i in range(len(L)):
				L[i]=float(L[i])
				soma=soma+float(L[i])
			if len(L) != 0 and len(L) != 1:
				Tc1.append(float(soma/(len(L))))
			else:
				Tc1.append(soma)
			N.append(int(len(L)))
	dic={}

	dic={"E":E, "Tc":Tc1, "N":N}

	# Create a list of tuples from the dictionary
	tuple_list = list(zip(dic["Tc"], dic["E"], dic["N"]))

	# Sort the list of tuples in descending order based on the values in the "Values" list
	sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

	# Create three lists from the sorted list of tuples
	sorted_Tc, sorted_E, sorted_N = zip(*sorted_list)

	# Update the dictionary with the sorted lists
	dic["E"] = sorted_E
	dic["Tc"] = sorted_Tc
	dic["N"] = sorted_N

	with open("1Element_Tc_sorted","w") as n:
		n.write("Element,Tc,Nº of Comps"+"\n")
		for i in range(len(dic["E"])):
			n.write(str(dic["E"][i])+","+str(dic["Tc"][i])+","+str(dic["N"][i])+"\n")
			
N=[]
Tc1=[]
with open("TcValues","r") as f:
	lines=f.readlines()
	for line in lines:
		if line == "\n":
			Tc1.append(0)
			N.append(0)
		else:
			line=line.strip("\n")
			L=line.split(",")
			L.pop(-1)
			soma=0
			c=0
			for i in range(len(L)):
				L[i]=float(L[i])
				if L[i] > 5:
					soma=soma+float(L[i])
					c=c+1
			if c != 0 and c != 1:
				Tc1.append(float(soma/c))
			else:
				Tc1.append(soma)
			N.append(int(c))
	dic={}

	dic={"E":E, "Tc":Tc1, "N":N}

	# Create a list of tuples from the dictionary
	tuple_list = list(zip(dic["Tc"], dic["E"], dic["N"]))

	# Sort the list of tuples in descending order based on the values in the "Values" list
	sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

	# Create three lists from the sorted list of tuples
	sorted_Tc, sorted_E, sorted_N = zip(*sorted_list)

	# Update the dictionary with the sorted lists
	dic["E"] = sorted_E
	dic["Tc"] = sorted_Tc
	dic["N"] = sorted_N

	with open("1Element_Tc5_sorted","w") as n:
		n.write("Element,Tc,Nº of Comps"+"\n")
		for i in range(len(dic["E"])):
			n.write(str(dic["E"][i])+","+str(dic["Tc"][i])+","+str(dic["N"][i])+"\n")
N=[]
Tc1=[]
with open("TcValues","r") as f:
	lines=f.readlines()
	for line in lines:
		if line == "\n":
			Tc1.append(0)
			N.append(0)
		else:
			line=line.strip("\n")
			L=line.split(",")
			L.pop(-1)
			soma=0
			c=0
			for i in range(len(L)):
				L[i]=float(L[i])
				if L[i] != 0.0:
					soma=soma+float(L[i])
					c=c+1
			if c != 0 and c != 1:
				Tc1.append(float(soma/c))
			else:
				Tc1.append(soma)
			N.append(int(c))
	dic={}

	dic={"E":E, "Tc":Tc1, "N":N}

	# Create a list of tuples from the dictionary
	tuple_list = list(zip(dic["Tc"], dic["E"], dic["N"]))

	# Sort the list of tuples in descending order based on the values in the "Values" list
	sorted_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

	# Create three lists from the sorted list of tuples
	sorted_Tc, sorted_E, sorted_N = zip(*sorted_list)

	# Update the dictionary with the sorted lists
	dic["E"] = sorted_E
	dic["Tc"] = sorted_Tc
	dic["N"] = sorted_N

	with open("1Elements_Tcex0_sorted","w") as n:
		n.write("Element,Tc,Nº of Comps"+"\n")
		for i in range(len(dic["E"])):
			n.write(str(dic["E"][i])+","+str(dic["Tc"][i])+","+str(dic["N"][i])+"\n")
p=0
q=0
with open("gil.csv","r") as a:
	lines = a.readlines()
	for i in range(1,len(lines)):
		line=lines[i]
		line=line.strip("\n")
		L=line.split(",")
		if float(L[2]) > 5:
			p=p+1
		if float(L[2]) != 0.0:
			q=q+1

print("Nº de Materiais com Tc>5: "+str(p))
print("Nº de Materiais com Tc>0: "+str(q))
