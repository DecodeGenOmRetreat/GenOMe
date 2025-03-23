##Basic
sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(f"The number of nucleotide A in sequence is :{sequence.count("A")}")
print(f"The number of nucleotide T in sequence is :{sequence.count("T")}")
print(f"The number of nucleotide G in sequence is :{sequence.count("G")}")
print(f"The number of nucleotide C in sequence is :{sequence.count("C")}")

print("\n")
## Function
def get_count(DNA):
    get_A = DNA.count("A")
    get_T = DNA.count("T")
    get_C = DNA.count("C")
    get_G = DNA.count("G")
    print(f"The number of nucleotide A in sequence is :{get_A}")
    print(f"The number of nucleotide T in sequence is :{get_T}")
    print(f"The number of nucleotide C in sequence is :{get_C}")
    print(f"The number of nucleotide G in sequence is :{get_G}")
get_count(sequence)
#print(f"The number of nucleotide A in sequence is :{a.get_A()}")
#print(f"The number of nucleotide T in sequence is :{sequence.count("T")}")
#print(f"The number of nucleotide G in sequence is :{sequence.count("G")}")
#print(f"The number of nucleotide C in sequence is :{sequence.count("C")}")

print("\n")
##Class
class Count:
    def __init__(self,DNA):
        self.DNA = DNA
        print(f"My DNA sequenc is :{self.DNA}")
    def get_count(self):
        get_A = self.DNA.count("A")
        get_T = self.DNA.count("T")
        get_C = self.DNA.count("C")
        get_G = self.DNA.count("G")
        return get_A, get_T,get_C,get_G 
a = Count("AGCTTTTCATTCTGACTGGGGGGGGGCAACCCCCCCCCCCCCGGGCAATATGTTTTTTTTTTTCTCTGTGTGGATTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAGTGTCTGATAGCAGC")
counts = a.get_count()
print(f"The number of nucleotide A in sequence is :{counts[0]}")
print(f"The number of nucleotide T in sequence is :{counts[1]}")
print(f"The number of nucleotide C in sequence is :{counts[2]}")
print(f"The number of nucleotide G in sequence is :{counts[3]}")
