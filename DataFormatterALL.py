from pymatgen.core import Composition
from tqdm import tqdm

mat_id=[] #list list of mat_id's
formula=[] #list of the chemical formulas
Tc=[] #list of the SC Tc's
Tc5=[] #list of the SC Tc's above 5K, all values below 5K are set to Zero
D=[] # ist of the ductability values
C=[] #list of the atomic fractions
C1=[] #list of the weight fractions
C2=[] #list of fraction in 0 or 1
E=[] #list of elements
N=0 #counter
M=0 #counter
O=0

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
	if float(L[2]) < 5:
		Tc5.append(0)
	else:
		Tc5.append(float(L[2]))	
	D.append(float(L[3]))
	
	
for i in formula:
	comp=Composition(i)
	CC=[]
	CC1=[]
	CC2=[]
	for j in E:
		CC.append(comp.get_atomic_fraction(j))
		CC1.append(comp.get_wt_fraction(j))
		if comp.get_atomic_fraction(j) > 0:
			CC2.append(1)
		else:
			CC2.append(0)
	C.append(CC)
	C1.append(CC1)
	C2.append(CC2)

Co = open("compfractionsatom","w") #list with the atomic fractions for each compound
Co1 = open("compfractionsweight","w") #list with the wt fractions for each compound
Cob = open("compfractionsbinary","w") #list with the binary fractions for each compound
Co2 = open("Ecomps","w") #list of each compound with each element
Co3 = open("Ecompsindex","w") #list of each compound index with each element
TcV = open("TcValues","w") #list of Tc values for each element
TcV5 = open("TcValues5","w") #list of Tc values above 5 for each element
DV = open("DValues","w") #list of D values for each element

for i in range(0,len(C)):
	for j in range(0,len(E)):
		Co.write(str(C[i][j])+",")
		Co1.write(str(C1[i][j])+",")
		Cob.write(str(C2[i][j])+",")
	Co.write("\n")
	Co1.write("\n")
	Cob.write("\n")

Co.close()
Co1.close()
Cob.close()
	
for i in range(0,len(E)):
	for j in range(0,len(C)):
		if C[j][i] != 0.0:
			Co2.write(str(formula[j])+",")
			Co3.write(str(j)+",")
			TcV.write(str(Tc[j])+",")
			TcV5.write(str(Tc5[j])+",")
			DV.write(str(D[j])+",")		
	Co2.write("\n")
	Co3.write("\n")
	TcV.write("\n")
	TcV5.write("\n")
	DV.write("\n")	
	
Co2.close()
Co3.close()
TcV.close()
DV.close()
	

TcVavg5 = open("TcValuesavg5","w") #list of avg Tc values above 5 for each element
TcVavgV5=0
	
TcVavg = open("TcValuesavg","w") #list of avg Tc values for each element
TcVavgV=0

TcVavgatomwv = open("TcValuesavgatomwv","w") #list of avg Tc values for each element
TcVavgVatomwv=0

TcVavgweightwv = open("TcValuesavgweightwv","w") #list of avg Tc values for each element
TcVavgVweightwv=0

DVavg = open("DValuesavg","w") #list of avg D values for each element
DVavgV=0

DVavgatomwv = open("DValuesavgatomwv","w") #list of avg D values for each element
DVavgVatomwv=0

DVavgweightwv = open("DValuesavgweightwv","w") #list of avg D values for each element
DVavgVweightwv=0	

###################################################################################

TcVavg5ex0 = open("TcValuesavg5ex0","w") #list of avg Tc values above 5 for each element
TcVavgV5ex0=0
	
TcVavgex0 = open("TcValuesavgex0","w") #list of avg Tc values for each element
TcVavgVex0=0

TcVavgatomwvex0 = open("TcValuesavgatomwvex0","w") #list of avg Tc values for each element
TcVavgVatomwvex0=0

TcVavgweightwvex0 = open("TcValuesavgweightwvex0","w") #list of avg Tc values for each element
TcVavgVweightwvex0=0

for i in tqdm(range(0,len(E))):
	for j in range(0,len(C)):
		if C[j][i] != 0.0:
			TcVavgV=TcVavgV+Tc[j]
			TcVavgV5=TcVavgV5+Tc5[j]
			TcVavgVatomwv=TcVavgVatomwv+(Tc[j]*C[j][i])
			TcVavgVweightwv=TcVavgVweightwv+(Tc[j]*C1[j][i])
			if float(Tc5[j]) > 0:
				TcVavgV5ex0=TcVavgV5ex0+Tc5[j]
				O=O+1
				
			if float(Tc[j]) > 0:	
				
				TcVavgVex0=TcVavgVex0+Tc[j]
				TcVavgVatomwvex0=TcVavgVatomwvex0+(Tc[j]*C[j][i])
				TcVavgVweightwvex0=TcVavgVweightwvex0+(Tc[j]*C1[j][i])
				M=M+1
				
			DVavgV=DVavgV+D[j]
			DVavgVatomwv=DVavgVatomwv+(D[j]*C[j][i])
			DVavgVweightwv=DVavgVweightwv+(D[j]*C1[j][i])
			N=N+1
			
			
	if N == 0:
		TcVavg.write("\n")
		TcVavg5.write("\n")
		TcVavgatomwv.write("\n")
		TcVavgweightwv.write("\n")
		DVavg.write("\n")
		DVavgatomwv.write("\n")
		DVavgweightwv.write("\n")
		
	if M == 0:
		TcVavgex0.write("\n")
		TcVavgatomwvex0.write("\n")
		TcVavgweightwvex0.write("\n")		
	
	if O == 0:
		TcVavg5ex0.write("\n")
	
	if N != 0:		
		TcVavgV=TcVavgV/N
		TcVavgV5=TcVavgV5/N
		TcVavgVatomwv=TcVavgVatomwv/N
		TcVavgVweightwv=TcVavgVweightwv/N
		DVavgV=DVavgV/N
		DVavgVatomwv=DVavgVatomwv/N
		DVavgVweightwv=DVavgVweightwv/N
		
		TcVavg.write(str(TcVavgV)+"\n")
		TcVavg5.write(str(TcVavgV5)+"\n")
		TcVavgatomwv.write(str(TcVavgVatomwv)+"\n")
		TcVavgweightwv.write(str(TcVavgVweightwv)+"\n")
		DVavg.write(str(DVavgV)+"\n")
		DVavgatomwv.write(str(DVavgVatomwv)+"\n")
		DVavgweightwv.write(str(DVavgVweightwv)+"\n")
		TcVavgV=0
		TcVavgVatomwv=0
		TcVavgVweightwv=0
		DVavgV=0
		DVavgVatomwv=0
		DVavgVweightwv=0
		N=0
		
	if M != 0:		
		TcVavgVex0=TcVavgVex0/M
		
		TcVavgVatomwvex0=TcVavgVatomwvex0/M
		TcVavgVweightwvex0=TcVavgVweightwvex0/M

		TcVavgex0.write(str(TcVavgVex0)+"\n")
		
		TcVavgatomwvex0.write(str(TcVavgVatomwvex0)+"\n")
		TcVavgweightwvex0.write(str(TcVavgVweightwvex0)+"\n")
		
		TcVavgVex0=0
		TcVavgVatomwvex0=0
		TcVavgVweightwvex0=0
		M=0
		
	if O != 0:
		TcVavgV5ex0=TcVavgV5ex0/O
		TcVavg5ex0.write(str(TcVavgV5ex0)+"\n")
		TcVavgV5ex0=0
		O=0
		
TcVavgex0.close()
TcVavg5ex0.close()
TcVavgatomwvex0.close()
TcVavgweightwvex0.close()
TcVavg.close()
TcVavg5.close()
TcVavgatomwv.close()
TcVavgweightwv.close()
DVavg.close()
DVavgatomwv.close()
DVavgweightwv.close()		
