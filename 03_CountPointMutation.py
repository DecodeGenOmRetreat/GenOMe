seq_1 = "GAGCCTACTAACGGGAT"
seq_2 = "CATCGTAATGACGGCCT"

if len(seq_1) != len(seq_2):
    print("length of sequence is not equal")
else:
    distance = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            distance = distance + 1      
    print (f"The hamming distance is :{distance}")

print("\n")

#function
def HammingDistance(seqA,seqB):
    if len(seqA)!= len(seqB):
        print("Both sequences is not equal in size")
    else:
        hammingDistance = 0
        for i in range(len(seq_1)):
            if seqA[i] != seqB:
                hammingDistance = hammingDistance + 1
        print(f"The count of point mutation is :{hammingDistance}")    
HammingDistance(seqA ="GAGCCTACTAACGGGAT",seqB ="CATCGTAATGACGGCCT")

#class
print("\n")
class CountPointMutation:
    def __init__(self,seqM,seqN):
        self.seqM = seqM
        self.seqN = seqN
        print(f"First sequence is : {self.seqM}")
        print(f"Second sequence is : {self.seqN}")
    def Distance(self):
        if len(self.seqM) !=len(self.seqN):
            print("Please enter sequences with eqaul in length")
        else:
            distanceHamming = 0
            for j in range(len(self.seqM)):
                if self.seqM != self.seqN:
                    distanceHamming += 1
            print(f"Hamming distance between two sequences is : {distanceHamming}")
a = CountPointMutation("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT")
a.Distance()