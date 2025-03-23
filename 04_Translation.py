sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
sequence = sequence.replace("U","T")
print(sequence)
last_codon = len(sequence)-2
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

protein = ""
for start in range(0,last_codon,3):
    codon = sequence[start:start+3]
    aa = gencode.get(codon)
    protein = protein + aa
    print(f"The codon of the given sequence is : {codon}")
print(f"Translated protein is : {protein}")
print("\n")


#Function

def Translation(rna):
    sequence = rna.replace("U","T")
    lastCodon = len(sequence)-2
    gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 
    'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T',
    'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K',
    'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 
    'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 
    'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 
    'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 
    'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 
    'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 
    'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 
    'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 
    'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 
    'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 
    'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'', 
    'TAG':'','TGC':'C', 'TGT':'C', 'TGA':'', 
    'TGG':'W'}
    protein = ""
    for start in range(0,lastCodon,3):
        codon = sequence[start:start+3]
        getAminoAcid = gencode.get(codon.upper())
        protein = protein + getAminoAcid
    print(f"Protein is :{protein}")

Translation("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

#Class
class Translation:
    def __init__(self,rna):
        self.rna = rna
        print(f"The name of RNA sequence :{self.rna}")
        self.gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 
        'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T',
        'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K',
        'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 
        'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 
        'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 
        'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 
        'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 
        'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V',
        'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 
        'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 
        'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 
        'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 
        'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 
        'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'', 
        'TAG':'','TGC':'C', 'TGT':'C', 'TGA':'', 
        'TGG':'W'}
    
    def getProtein(self):
        RNAtoDNA = self.rna.replace("U","T")
        lastCodon = len(RNAtoDNA)-2
        Proteincodon = ""
        for start in range(0,lastCodon,3):
            codon = RNAtoDNA[start:start+3]
            getTranslation = self.gencode.get(codon.upper())
            Proteincodon = Proteincodon + getTranslation
        print(f"The protien coding is : {Proteincodon}")
            #return Proteincodon

a = Translation("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
a.getProtein()       



