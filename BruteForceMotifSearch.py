from itertools import product

#calculate the score of list of motifs
def calculateScore(motif_position,t,n,k,dna_sequences):
    score=0
    for d in range(0,k):#the step in each sequence 
        frequecy={'A':0,'T':0,'G':0,'C':0}#frequence array for each dna element
        for row in range(0,t):
            col=motif_position[row]+d#current col= step+start_position which is motif_pos in the current row
            cur_c=dna_sequences[row][col]#current element at that position
            frequecy[cur_c]=frequecy[cur_c]+1#increase frequency
        #sort frequency to get element with maximum frequency
        sorted_frequency = sorted(frequecy.items(), key=lambda x: x[1] , reverse=True)    
        current_score=0
        #current score is sum of frequencies of remaining elements except the one with max frequency
        for i in range(1,4):
            current_score=current_score+sorted_frequency[i][1]
        #accumulate the score for each column 
        score=score+current_score
    return score

#extract the k mers starting from best_motif_pos
def getKMers(best_motif_pos,n,t,k,dna_sequences):
    k_mers=[]
    #loop through all sequences
    for row in range(0,t):
        #best_motif_pos is in the format (s0,s1....,s(t-1)) for all rows from 0 to (t-1)
        #start post
        start_pos=best_motif_pos[row]
        #end pos
        end_pos=start_pos+k
        #motif from start_pos to end_pos
        motif=dna_sequences[row][start_pos:end_pos]
        #append motif to the result
        k_mers.append(motif)
    #print the result
    for motif in k_mers:
        print(motif)
    

def BruteForceMotifSearch(dna_sequences,n,t,k):
    #generate all different combinaation (s0,s1....,s(t-1)) where  0=<si<=n-k+1
    motifs_position = [ele for ele in product(range(0, n-k+1), repeat = t)]
    #best motif positions par default equal to first motifs_position
    best_motif_pos=motifs_position[0]
    #initialize best_score with greatest value in our case the maximum is t*n
    best_score=t*n;
    for motif_position in motifs_position:
        #calculate score
        current_score=calculateScore(motif_position,t,n,k,dna_sequences)
        #update best_score and best_motif
        if current_score<=best_score:
            best_score=current_score
            best_motif_pos=motif_position
    
    getKMers(best_motif_pos,n,t,k,dna_sequences)



def main():
    #open file
    file = open('dna_input.txt','r')
    dna_sequences=[]
    m=[]
    line_number=0
    t=0
    k=0
    n=0
    for line in file:
        line=line.strip()
        #if it's first line read k,t
        if line_number==0:
            k,t=int(line.split(" ")[0]),int(line.split(" ")[1])
        else:
            #append to the dna_sequences the current sequence(line)
            dna_sequences.append(line)
            n=len(line)
        line_number=line_number+1

    
    BruteForceMotifSearch(dna_sequences,n,t,k)


if __name__ == "__main__":
    main()



