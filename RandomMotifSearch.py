from random import randint


#calculate mismatch
def calcMismatch(seq1, seq2):
    assert len(seq1) == len(seq2)
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist

def GenerateProfileDict(matrix, j):
    return {'A': matrix[0][j], 'C': matrix[1][j], 'G': matrix[2][j], 'T': matrix[3][j]}

#find most probable kmer
def FindMostProbableKmer(dna_sequence, k, matrix):
    maxPr = 0
    prList = []
    for i in range(len(dna_sequence)-k+1):
        KmerPr = 1
        pattern = dna_sequence[i:i+k]
        # print pattern
        for j in range(len(pattern)):
            profile = GenerateProfileDict(matrix, j)
            # print profile
            KmerPr *= profile[pattern[j]]
        # print "KmerPr =", KmerPr
        prList.append(KmerPr)
    i = prList.index(max(prList))
    maxKmer = dna_sequence[i:i+k]
    return maxKmer





def score(motifs):
    '''Returns the score of the dna_sequences list motifs.'''
    score = 0
    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        # Calculate the min score between motif and [AAAAA, CCCCC, GGGGG, TTTTT]
        score += min([calcMismatch(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
    return score


def GenerateProfileMatWithPesudoCount(dna_sequences,t):
    seqNum = float(t)
    dna_elements = ['A', 'C', 'G', 'T']
    matrix = []
    for i in range(len(dna_sequences[0])):
        base_i = [seq[i] for seq in dna_sequences]
        # print base_i
        # print "seqNum = ", seqNum + 4
        colProfile = [float(base_i.count(n) + 1)/float(seqNum + 4) for n in dna_elements]
        # print "colProfile = ", colProfile
        matrix.append(colProfile)
    return [list(i) for i in zip(*matrix)]


def RandomizedMotifSearchIteration(dna_sequences, k,t):
    # Random select initial motifs
    kmerIndex = [randint(0, len(dna_sequences[0]) - k) for i in range(t)]
    #extract the randomly selected motifs
    Motifs = [dna_sequences[i][j:j+k] for i, j in enumerate(kmerIndex)]
    #initialize bestMotifs and best_score
    BestMotifs = Motifs
    best_score=score(BestMotifs);

    while True:
        #generate the profile
        ProfileMatrix = GenerateProfileMatWithPesudoCount(Motifs,t)
        #extract the motifs
        Motifs = [FindMostProbableKmer(dna_sequences[i], k, ProfileMatrix) for i in range(t)]
        #calculate score of obtained motifs
        current_score=score(Motifs)
        #update best_score and BestMotifs
        if current_score <best_score :
            best_score=current_score
            BestMotifs = Motifs
        else:
            return best_score,BestMotifs

def RandomizedMotifSearch(dna_sequences,k,t,n):
    BestMotifs=[]
    #set best_score to max value
    best_score=t*n
    #run the RandomizedMotifSearchIteration 1000 times
    for iteration in range(0,1000):
        iteration_score,iteration_motifs=RandomizedMotifSearchIteration(dna_sequences, k,t)
        #update best score  nd bestMotifs
        if iteration_score<best_score:
            best_score=iteration_score
            BestMotifs=iteration_motifs
    #print(best_score)
    for motif in BestMotifs:
        print(motif)


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
    RandomizedMotifSearch(dna_sequences, k,t,n)


if __name__ == "__main__":
    main()

