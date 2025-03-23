#
fasta = open(input("Enter your fasta file : "))
fasta = fasta.readlines()
dna_string = []
for i in fasta:
    if not i.startswith(">"):
        i = i.rstrip()
        dna_string.append(i)
print( f"Here is your input sequence :{dna_string}")

length = len(dna_string[0])  
A_count = [0]* length
T_count = [0]* length
C_count = [0]* length
G_count = [0]* length
profile = []

for sequence in dna_string:
    for i in range(length):
        if sequence[i] == "A":
            A_count[i] += 1
        elif sequence[i] == "T":
            T_count[i] += 1
        elif sequence[i] == "C":
            C_count[i] += 1
        elif sequence[i] == "G":
            G_count[i] += 1
        else:
            pass
profile.append(A_count)
profile.append(T_count)
profile.append(C_count)
profile.append(G_count)
print(f"Here is your profile matrix :{profile}")

#consensus
sublist= [[] for _ in range(length)]
for i in profile:
    for j in range(length):
        a = i[j]
        sublist[j].append(a) 

consensus = []
for k in sublist:
    if k.index(max(k)) ==0:
        consensus.append("A")
    elif k.index(max(k))== 1:
        consensus.append("T")
    elif k.index(max(k))== 2:
        consensus.append("C")
    elif k.index(max(k))== 3:
        consensus.append("G")
print(f"Here is your consensus :{"".join(consensus)}")
 

# Function
def consensus(fastafile):
    fasta = open(fastafile)
    fasta = fasta.readlines()
    dna_string = []
    for i in fasta:
        if not i.startswith(">"):
            i = i.rstrip()
            dna_string.append(i)
    print( f"Here is your input sequence :{dna_string}")
    length = len(dna_string[0])  
    A_count = [0]* length
    T_count = [0]* length
    C_count = [0]* length
    G_count = [0]* length
    profile = []
    for sequence in dna_string:
        for i in range(length):
            if sequence[i] == "A":
                A_count[i] += 1
            elif sequence[i] == "T":
                T_count[i] += 1
            elif sequence[i] == "C":
                C_count[i] += 1
            elif sequence[i] == "G":
                G_count[i] += 1
            else:
                pass
    profile.append(A_count)
    profile.append(T_count)
    profile.append(C_count)
    profile.append(G_count)
    print(f"Here is your profile matrix :{profile}")

#consensus
    sublist= [[] for _ in range(length)]
    for i in profile:
        for j in range(length):
            a = i[j]
            sublist[j].append(a) 

    consensus = []
    for k in sublist:
        if k.index(max(k)) ==0:
            consensus.append("A")
        elif k.index(max(k))== 1:
            consensus.append("T")
        elif k.index(max(k))== 2:
            consensus.append("C")
        elif k.index(max(k))== 3:
            consensus.append("G")
    print(f"Here is your consensus :{"".join(consensus)}")
 
consensus("dna.fasta")


# Class
#class consensus:
#    def __init__(self,fastafile):
#        self.fastafile = fastafile
        









