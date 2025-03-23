seq = "GATATATGCATATACTT"
targetseq = "ATAT"
seqlen = len(seq)
for start in range(seqlen):
    subseq = seq[start:start+4]
    print(f"The sequence is : {subseq}")
    if targetseq in subseq:
        print(f"The index of {targetseq} is :{start + 1}")

#Alternatives

print("\n")

for start in range(seqlen):
    subseq= seq[start:seqlen]
    print(f"The sequence is :{subseq}")
    if subseq.startswith(targetseq):
        print(f"the index of {targetseq} is: {start + 1}")  


#Functions
print("\n")
def motiF(sequence, subsequence):
    lenSeq = len(sequence)
    for start in range(lenSeq):
        seqSub = sequence[start:lenSeq]
        print(f"The sequence is : {seqSub}")
        if seqSub.startswith(subsequence):
            print(f"The index of {subsequence} is : {start+1}")
motiF(sequence = "GATATATGCATATACTT", subsequence = "ATAT")


#Class 
