
## Amino acids and their corresponding codons

MET = "AUG"; ARG = "AGA"; ASP = "GAU"; VAL = "GUC"; HIS = "CAC"; ALA = "GCA" 
GLY = "GGU"; TYR = "UAU"; ASN = "AAU"; ILE = "AUU"; SER = "AGU"; THR = "ACC"

## DNA sequence

raw_data = "Data Bank Entry T-A-T-T-A-A-C-T-C-G-C-C-G-C-T-A-C-T-G-G-C-C-A-C-A-G-T-A-A-C-G-T-C-T-A-A-T-A-T-T-A-A-T-C-G-C-C-G-C-G-C Data Bank Entry"
index= raw_data.find("-") -1
finalindex= raw_data.rfind("-")+1
newrawdata=raw_data[index:finalindex+1]
dnalist=newrawdata.split("-")
dna="".join(dnalist)
index1= dna.find("TAC")
lst=[]
for i in range(index1,len(dna),3):
    if dna[i:i+3]=="ATT" or  dna[i:i+3]=="ATC"or  dna[i:i+3]=="ACT":
        lst.append(i)
#lst1=eval(lst)
index2=(lst)+3
dnanew=dna[index1:index2]
print(dnanew)
mrna=""
for letter in dnanew:
    if letter == "A":
        mrna +="U"
    elif letter =="G":
        mrna += "C"
    elif letter == "C":
        mrna += "G"
    else:
        mrna +="A"
print(mrna)
for i in range(,len(mrna),3):
    mrna[i:i+3]


