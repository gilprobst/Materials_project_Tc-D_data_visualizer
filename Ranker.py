E1=[]
e = open("elementslist","r")

lines = e.readlines()

for line in lines:
    line=line.strip(" \n")
    E1.append(line)

e.close()

D=[]
E=[]
N=[]

with open("DValues","r") as a:
	lines=a.readlines()
	for i,line in enumerate(lines):
		if line != "\n":
			line=line.strip("\n")
			L=line.split(",")
			L.pop(-1)
			soma=0
			for i in range(len(L)):
				soma=soma+float(L[i])
			D.append(soma/len(L))
			E.append(E1[i])
			N.append(len(L))
			
			
	dic={}	
	dic={"E":E, "D":D, "N":N}

	# Create a list of tuples from the dictionary
	tuple_list = list(zip(dic["E"], dic["D"], dic["N"]))

	# Sort the list of tuples in descending order based on the values in the "Values" list
	sorted_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)

	# Create three lists from the sorted list of tuples
	sorted_E, sorted_D, sorted_N= zip(*sorted_list)

	# Update the dictionary with the sorted lists
	dic["E"] = sorted_E
	dic["D"] = sorted_D
	dic["N"] = sorted_N

	with open("1Element_D_ranked","w") as n:
			n.write("Element,Avg D,Nº of Comps"+"\n")
			for i in range(len(dic["E"])):
				n.write(str(dic["E"][i])+","+str(dic["D"][i])+","+str(dic["N"][i])+"\n")
	
##########################################################################################################################################
E2=[]
for i in range(len(E1)):
	for j in range(len(E1)):
		if i<=j:
			E2.append(E1[i]+"-"+E1[j])
D=[]
N=[]

with open("2ElementsNdata","r") as a:
	lines=a.readlines()
	for i,line in enumerate(lines):
		line=line.strip("\n")
		L=line.split(",")
		print(len(L))
		for j in range(len(L)):
			if i<=j:
				N.append(int(L[j]))

with open("2ElementsDdata","r") as a:
	lines=a.readlines()
	for i,line in enumerate(lines):
		line=line.strip("\n")
		L=line.split(",")
		print(len(L))
		for j in range(len(L)):
			if i<=j:
				D.append(float(L[j]))
	print(len(E2))
	print(len(D))		
	dic={}	
	dic={"E":E2, "D":D, "N":N}

	# Create a list of tuples from the dictionary
	tuple_list = list(zip(dic["E"], dic["D"], dic["N"]))

	# Sort the list of tuples in descending order based on the values in the "Values" list
	sorted_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)

	# Create three lists from the sorted list of tuples
	sorted_E, sorted_D, sorted_N= zip(*sorted_list)

	# Update the dictionary with the sorted lists
	dic["E"] = sorted_E
	dic["D"] = sorted_D
	dic["N"] = sorted_N

	with open("2Elements_D_ranked","w") as n:
		n.write("Combination of Element,Avg D,Nº of Comps"+"\n")
		for i in range(len(dic["E"])):
			n.write(str(dic["E"][i])+","+str(dic["D"][i])+","+str(dic["N"][i])+"\n")
