filename = open(input("Enter the sequence file :"))
fasta = filename.readlines()
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W'}

sequences = []
for line in fasta:    
    if not line.startswith(">"):
        line= line.rstrip("\n")
        print(f"The length of sequence : {len(line)}")
        sequences.append(line)
print(f"Given sequences :{sequences}")

proteins = []
for seq in sequences:
    for frame in range(3):
        dna = seq[frame:]
        #print(dna)
        for i in range(0,len(dna)-2,3):
            codon = dna[i:i+3]
            protein = ""
            #print(f"print {codon}")
            if codon == "ATG":
                for j in range(i,len(dna)-2,3):
                    value = gencode.get(dna[j:j+3])
                    protein += str(value) 
                    if value == "":
                        proteins.append(protein)
                        break               
print(f"The open reading frame is : {proteins}")
#print(len(proteins))
