from pymatgen.core import Composition

mat_id=[] #list list of mat_id's
formula=[] #list of the chemical formulas
Tc=[] #list of the SC Tc's
D=[] # ist of the ductability values
C=[] #list of the atomic fractions
C1=[] #list of the weight fractions
E=[] #list of elements
N=0 #counter

f = open("elementslist","r")

lines = f.readlines()

for line in lines:
    line=line.strip(" \n")
    E.append(line)
    
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
	CC1=[]
	for j in E:
		CC.append(comp.get_atomic_fraction(j))
		CC1.append(comp.get_wt_fraction(j))
	C.append(CC)
	C1.append(CC1)

Co = open("compfractionsatom","w") #list with the atomic fractions for each compound
Co1 = open("compfractionsweight","w") #list with the wt fractions for each compound
Co2 = open("Ecomps","w") #list of each compound with each element
Co3 = open("Ecompsindex","w") #list of each compound index with each element
DV = open("DValues","w") #list of D values for each element

for i in range(0,len(C)):
	for j in range(0,len(E)):
		Co.write(str(C[i][j])+",")
		Co1.write(str(C1[i][j])+",")
	Co.write("\n")
	Co1.write("\n")

Co.close()
Co1.close()
	
for i in range(0,len(E)):
	for j in range(0,len(C)):
		if C[j][i] != 0.0:
			Co2.write(str(formula[j])+",")
			Co3.write(str(j)+",")
			DV.write(str(D[j])+",")		
	Co2.write("\n")
	Co3.write("\n")
	DV.write("\n")	
	
Co2.close()
Co3.close()
DV.close()


DVavg = open("DValuesavg","w") #list of avg D values for each element
DVavgV=0

DVavgatomwv = open("DValuesavgatomwv","w") #list of avg D values for each element
DVavgVatomwv=0

DVavgweightwv = open("DValuesavgweightwv","w") #list of avg D values for each element
DVavgVweightwv=0	

for i in range(0,len(E)):
	for j in range(0,len(C)):
		if C[j][i] != 0.0:
			DVavgV=DVavgV+D[j]
			DVavgVatomwv=DVavgVatomwv+(D[j]*C[j][i])
			DVavgVweightwv=DVavgVweightwv+(D[j]*C1[j][i])
			N=N+1
	if N == 0:
		DVavg.write("\n")
		DVavgatomwv.write("\n")
		DVavgweightwv.write("\n")
	
	if N != 0:		
		DVavgV=DVavgV/N
		DVavgVatomwv=DVavgVatomwv/N
		DVavgVweightwv=DVavgVweightwv/N
		
		DVavg.write(str(DVavgV)+"\n")
		DVavgatomwv.write(str(DVavgVatomwv)+"\n")
		DVavgweightwv.write(str(DVavgVweightwv)+"\n")

		DVavgV=0
		DVavgVatomwv=0
		DVavgVweightwv=0
		N=0
		
DVavg.close()
DVavgatomwv.close()
DVavgweightwv.close()		
