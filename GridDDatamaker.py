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
Dboth=[]
Dboth1=[]
N=[]
N1=[]
	    
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
		Dboth1.append(0)
	Dboth.append(Dboth1)
	Dboth1=[]

M=[]

for i in range(len(EC3)):
	A=EC3[i]
	dummy=[]
	for j in range(len(EC3)):
		B=EC3[j]
		N=0
		for l in A:
			for k in B:	
				if l == k:
					N=N+1
					Dboth[i][j]=float(Dboth[i][j])+float(D[k])
					
		if N != 0:
			Dboth[i][j]=Dboth[i][j]/N
		dummy.append(N)
	M.append(dummy)
Elements1=E
Elements2=E

		

y = open("2ElementsNdata","w")

for i in range(len(M)):
	for j in range(len(M[i])):
		#Dboth[i][j]=Dboth[i][j]*0.5 #to fix the double counting done before
		if j != len(M[i])-1:
			y.write(str(M[i][j])+",")
		else:
			y.write(str(M[i][j]))
		
	y.write("\n")
y.close()


z = open("2ElementsDdata","w")

for i in range(len(Dboth)):
	for j in range(len(Dboth[i])):
		#Dboth[i][j]=Dboth[i][j]*0.5 #to fix the double counting done before
		if j != len(Dboth[i])-1:
			z.write(str(Dboth[i][j])+",")
		else:
			z.write(str(Dboth[i][j]))
		
	z.write("\n")
z.close()
