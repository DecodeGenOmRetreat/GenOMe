FastaFile = open(input("Enter the sequence file :"))
readSeq = FastaFile.readlines()
FastaFile.close()
sequences = []
for seq in readSeq:
    if not seq.startswith(">"):
        seq = seq.rstrip("\n")
        sequences.append(seq)
print(sequences)

minLen = 0
smallSeq = ''
for seq in sequences:
    print(seq)
    if minLen <= len(seq):
        minLen = len(seq)
    else:
        minLen = len(seq)
        smallSeq = str(seq) 

print(minLen)
print(smallSeq)


for start in range(len(smallSeq)-1):
    i = smallSeq[start:start + 2]
    print(i)
