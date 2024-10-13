

#generate profil with pseudo count
def GenerateProfileMatWithPesudoCount(dna):
    seqNum = float(len(dna))
    dna_elements = ['A', 'C', 'G', 'T']
    matrix = []
    for i in range(len(dna[0])):
        base_i = [seq[i] for seq in dna]
        colProfile = [float(base_i.count(n) + 1)/seqNum + 4 for n in dna_elements]
        matrix.append(colProfile)
    return [list(i) for i in zip(*matrix)]

#calculate mismatch between tow sequences
def calcMismatch(seq1, seq2):
    assert len(seq1) == len(seq2)
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist

def GenerateProfileDict(matrix, j):
    return {'A': matrix[0][j], 'C': matrix[1][j], 'G': matrix[2][j], 'T': matrix[3][j]}


def score(motifs):
    '''Returns the score of the dna list motifs.'''
    score = 0
    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        # Calculate the min score between motif and [AAAAA, CCCCC, GGGGG, TTTTT]
        # avoiding find the consensus strings
        score += min([calcMismatch(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
    return score


def FindMostProbableKmers(text, k, matrix):
    # print text
    maxPr = 0
    prList = []
    for i in range(len(text)-k+1):
        KmerPr = 1
        pattern = text[i:i+k]
        # print pattern
        for j in range(len(pattern)):
            profile = GenerateProfileDict(matrix, j)
            # print profile
            KmerPr *= profile[pattern[j]]
        # print "KmerPr =", KmerPr
        prList.append(KmerPr)
    i = prList.index(max(prList))
    maxKmer = text[i:i+k]
    return maxKmer



def GreedyMotifSearch(dna, k, t):
    #best motifs initially are first motifs in each row
    BestMotifs = [seq[0:k] for seq in dna]
    seq = dna[0]
    # print seq
    for i in range(len(seq) - k):
        kmers = seq[i:i+k]
        
        motifs = [kmers]
        for j in range(1, len(dna)):
            #generate Profile with pseudo count
            mat = GenerateProfileMatWithPesudoCount(motifs)
            # print "Find Portable Kmer:"
            #find the most probable kmer in the current row j
            tempMotif = FindMostProbableKmers(dna[j], k, mat)
            motifs.append(tempMotif)
        #update score
        if score(motifs) < score(BestMotifs):
            BestMotifs = motifs
    for motif in BestMotifs:
        print(motif)
    return BestMotifs



def main():
    file = open('dna_input.txt','r')
    dna_sequences=[]
    m=[]
    line_number=0
    t=0
    k=0
    n=0
    for line in file:
        line=line.strip()
        if line_number==0:
            k,t=int(line.split(" ")[0]),int(line.split(" ")[1])
        else:
            dna_sequences.append(line)
            n=len(line)
        line_number=line_number+1
    GreedyMotifSearch(dna_sequences, k, t)


if __name__ == "__main__":
    main()



