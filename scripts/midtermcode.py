import csv
from pathlib import Path
base = Path(__file__).resolve().parent
resDir = (base.parent / 'results').resolve()
dataDir = (base.parent / 'data').resolve()

#count how many times each amino acid appears, add to a dictionary
def amino_acids(prot):
    aa = {}
    for letter in prot:
        aa[letter] = aa.get(letter, 0) + 1
    return aa


file1 = open(dataDir / "exterme_organism_proteins.txt", "r")
org_prot = {}
current_org = ""
current_seq = ""

for line in file1:
    line = line.strip()
    if line.startswith(">"):
        #if the organism is new, add the current sequence to the dictionary (as value- key=organism)
        if current_org != "":
            org_prot[current_org] = current_seq
            current_seq = ""
            
        #get the organism's name
        if "OS=" in line:
            start = line.index("OS=") + 3
            rest = line[start:].split()
            current_org = rest[0] + " " + rest[1]
    else:
        current_seq += line

#last organism
if current_org != "":
    org_prot[current_org] = current_seq

file1.close()


output = open(resDir / 'amino_acid_composition.csv', 'w', newline='')
writer = csv.writer(output)

#list of amino acids
amino_list = list("ACDEFGHIKLMNPQRSTVWY")

writer.writerow(["Organism"] + amino_list)

#percentage calculations and prints in csv file
for org, seq in org_prot.items():
    prots = amino_acids(seq)
    total_len = len(seq)

    row = [org]
    
    for aa in amino_list:
        count = prots.get(aa, 0)
        percent = (count / total_len) * 100 if total_len > 0 else 0.0
        row.append(f"{percent:.2f}%")

    writer.writerow(row)

output.close()
print(f"Wrote output to: {resDir / 'amino_acid_composition.csv'}")