DNA = "GATGGAACTTGACTACGTAAATT"
print(f"Given DNA is :{DNA}")
RNA = DNA.replace("T","U")
print(f"Transcribed RNA is :{RNA}")

#Function
print("\n")
def TransciptionFun(DNA):
    print(f"Given DNA is :{DNA}")
    RNA = DNA.replace("T","U")
    print(f"Transcribed RNA is :{RNA}")
    return DNA
TransciptionFun("GATGGAACTTGACTACGTAAATT")

#Class
print("\n")
class TranscriptionClass:
    def __init__(self, Sequence):
        self.Sequence = Sequence
        print(f"Given DNA is :{self.Sequence}")

    def Transciption(self):
        RNA = self.Sequence.replace("T","U")
        print(f"Transcribed RNA is :{RNA}")
        return RNA;
a = TranscriptionClass("GATGGAACTTGACTACGTAAATT")
a.Transciption()