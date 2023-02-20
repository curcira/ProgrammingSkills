import sys
import re

from Bio import SeqIO
from statistics import mean


def readFASTA(FileName):
    (n, d, s) = ([], [], [])
    file_handler = open(FileName, "r")
    for multi_seqs in SeqIO.parse(file_handler, "fasta"):
        n.append(multi_seqs.id)
        d.append(multi_seqs.description)
        s.append(multi_seqs.seq)
    return n, d, s

def translation(Sequence):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    }
    protein = ""
    for i in range(0, len(Sequence) - 2, 3):
        codon = Sequence[i:i + 3]
        protein += table[codon]

    return protein


def gcContent(Sequence):
    GC_content = (Sequence.count("G") + Sequence.count("C")) \
                 / len(Sequence) * 100
    GC_content = round(GC_content, 2)
    return GC_content


def getMax(x, y):
    max_num = max(y)
    max_length = []
    for i in range(len(x)):
        if y[i] == max_num:
            max_length.append(x[i])
            max_length.append(y[i])
    max_length = tuple(max_length)
    return max_length


def getMin(x, y):
    min_num = min(y)
    min_length = []
    for i in range(len(x)):
        if y[i] == min_num:
            min_length.append(x[i])
            min_length.append(y[i])
    min_length = tuple(min_length)
    return min_length


def getAverage(x, y):
    avg = mean(y)
    avg = round(avg, 2)
    return avg


def nucleotide_counter1(Seq):
    myD = {}
    for i in range(0, len(Seq)):
        di = Seq[i]
        if myD.get(di, 0) == 0:
            myD[di] = 1
        else:
            myD[di] = myD[di] + 1
    return myD


def get_codon1(Seq):
    myD = {}
    for i in range(0, len(Seq) - 2):
        di = Seq[i:i + 3]
        if myD.get(di, 0) == 0:
            myD[di] = 1
        else:
            myD[di] = myD[di] + 1
    return myD

def findCommon(x,y):
   x = set(x)
   y = set(y)
   if len(x.intersection(y)) > 0:
       return x.intersection(y)

def findCommon0(x,y):
    result = []
    for i in x:
        if i in y:
            result.append(i)
    return result

def findUnique(x,y):
    x = set(x)
    y = set(y)
    x_unique = x.difference(y)
    y_unique = y.difference(x)
    return x_unique, y_unique

def findUnique0(x,y):
    x_unique0 = []
    y_unique0 = []
    for i in x:
        if i not in y:
            x_unique0.append(i)
    for i in y:
        if i not in x:
            y_unique0.append(i)
    return x_unique0, y_unique0

def enzymeFinder(rest,seq):
    restriction = rest
    sequence = str(seq)
    count = 0
    myD={}
    for match in re.finditer(restriction, sequence):
        start = match.start()
        end = match.end()
        count = count+1
        myD[count] = [start,end]
    return myD


## main program
name = 'Rachel Curci'
print("Welcome! I am {0}\n".format(name))
x1 = input("Input the 1st file argument you would like to compare")
x1 = int(x1)
y2 = input("Input the 2nd file argument you would like to compare")
y2 = int(y2)
x = sys.argv[x1]
y = sys.argv[y2]
print("The 1st File Name is ({0})\n".format(x))
print("The 2nd File Name is ({0})\n".format(y))
print("[Part 1] Summary Information\n")
File1 = readFASTA(x)
total1 = len(File1[0])
names1 = File1[0]
desc1 = File1[1]
seqs1 = File1[2]
print("(1) The 1st File:")
print("(A) There are a total of ({0}) sequences in the file".format(total1))
gc_list1 = []
lengths_list1 = []
count_A_list1 = []
count_T_list1 = []
count_G_list1 = []
count_C_list1 = []
for i in range(len(seqs1)):
    gc1 = gcContent(seqs1[i])
    gc_list1.append(gc1)
    lengths1 = len(seqs1[i])
    lengths_list1.append(lengths1)
    counts_1 = nucleotide_counter1(seqs1[i])
    for key, value in counts_1.items():
        if key == 'A':
            count_A_list1.append(value)
        elif key == 'T':
            count_T_list1.append(value)
        elif key =='G':
            count_G_list1.append(value)
        elif key == 'C':
            count_C_list1.append(value)
length_avg1 = getAverage(names1, lengths_list1)
length_min1 = getMin(names1, lengths_list1)
length_max1 = getMax(names1, lengths_list1)
count_A_max1 = getMax(names1, count_A_list1)
count_T_max1 = getMax(names1, count_T_list1)
count_G_max1 = getMax(names1, count_G_list1)
count_C_max1 = getMax(names1, count_C_list1)
gc_max1 = getMax(names1, gc_list1)
gc_min1 = getMin(names1, gc_list1)
gc_avg1 = getAverage(names1, gc_list1)
print("(B) The average length of all the sequences is ({0})".format(length_avg1))
print("(C) The longest sequence is ({0}), length = [{1}]".format(length_max1[0], length_max1[1]))
print("(D) The shortest sequence is ({0}), length = [{1}]".format(length_min1[0], length_min1[1]))
print("(E) The sequence that contains the most Adenine is ({0}), count=[{1}]".format(count_A_max1[0], count_A_max1[1]))
print("(F) The sequence that contains the most Thymine is ({0}), count=[{1}]".format(count_T_max1[0], count_T_max1[1]))
print("(G) The sequence that contains the most Guanine is ({0}), count=[{1}]".format(count_G_max1[0], count_G_max1[1]))
print("(H) The sequence that contains the most Cytosine is ({0}), count=[{1}]".format(count_C_max1[0], count_C_max1[1]))
print("(I) The sequence that contains the highest GC content is ({0}), GC content=[{1}%]".format(gc_max1[0], gc_max1[1]))
print("(J) The sequence that contains the lowest GC content is ({0}), GC content=[{1}%]".format(gc_min1[0], gc_min1[1]))
print("(K) The average GC content for all sequences is ({0}%)\n".format(gc_avg1))
File2 = readFASTA(y)
total2 = len(File2[0])
names2 = File2[0]
desc2 = File2[1]
seqs2 = File2[2]
print("(2) The 2nd File:")
print("(A) There are a total of ({0}) sequences in the file".format(total2))
gc_list2 = []
lengths_list2 = []
count_A_list2 = []
count_T_list2 = []
count_G_list2 = []
count_C_list2 = []
for i in range(len(seqs2)):
    gc2 = gcContent(seqs2[i])
    gc_list2.append(gc2)
    lengths2 = len(seqs2[i])
    lengths_list2.append(lengths2)
    lengths_list2 = list(lengths_list2)
    counts_2 = nucleotide_counter1(seqs2[i])
    for key, value in counts_2.items():
        if key == 'A':
            count_A_list2.append(value)
        elif key == 'T':
            count_T_list2.append(value)
        elif key =='G':
            count_G_list2.append(value)
        elif key == 'C':
            count_C_list2.append(value)
length_avg2 = getAverage(names2, lengths_list2)
length_min2 = getMin(names2, lengths_list2)
length_max2 = getMax(names2, lengths_list2)
count_A_max2 = getMax(names2, count_A_list2)
count_T_max2 = getMax(names2, count_T_list2)
count_G_max2 = getMax(names2, count_G_list2)
count_C_max2 = getMax(names2, count_C_list2)
gc_max2 = getMax(names2, gc_list2)
gc_min2 = getMin(names2, gc_list2)
gc_avg2 = getAverage(names2, gc_list2)
print("(B) The average length of all the sequences is ({0})".format(length_avg2))
print("(C) The longest sequence is ({0}), length = [{1}]".format(length_max2[0], length_max2[1]))
print("(D) The shortest sequence is ({0}), length = [{1}]".format(length_min2[0], length_min2[1]))
print("(E) The sequence that contains the most Adenine is ({0}), count=[{1}]".format(count_A_max2[0], count_A_max2[1]))
print("(F) The sequence that contains the most Thymine is ({0}), count=[{1}]".format(count_T_max2[0], count_T_max2[1]))
print("(G) The sequence that contains the most Guanine is ({0}), count=[{1}]".format(count_G_max2[0], count_G_max2[1]))
print("(H) The sequence that contains the most Cytosine is ({0}), count=[{1}]".format(count_C_max2[0], count_C_max2[1]))
print("(I) The sequence that contains the highest GC content is ({0}), GC content=[{1}%]".format(gc_max2[0], gc_max2[1]))
print("(J) The sequence that contains the lowest GC content is ({0}), GC content=[{1}%]".format(gc_min2[0], gc_min2[1]))
print("(K) The average GC content for all sequences is ({0}%)\n".format(gc_avg2))

sim = findCommon(names1, names2)
sim0 = findCommon0(names1, names2)
print("(3) The sequences common in both files:")
print(', '.join(str(x) for x in sim))
print("")

unique = findUnique(names1, names2)
unique0 = findUnique0(names1, names2)
F1_unique = unique[0]
print("(4) The sequences unique in the 1st file:")
print(', '.join(str(x) for x in F1_unique))
print("")
F2_unique = unique[1]
print("(5) The sequences unique in the 2nd file:")
print(', '.join(str(x) for x in F2_unique))
print("")
print("[Part 2] Examine individual sequence")
names = names1
for x in names2:
    if x not in names1:
        names.append(x)


desc = desc1
for x in desc2:
    if x not in desc1:
        desc.append(x)


seqs = seqs1
for x in seqs2:
    if x not in seqs1:
        seqs.append(x)

while True:
    user_sequence = input("Question 1: Which sequence do you want to see ('q' for exit)?")
    if user_sequence == 'q':
        exit()
    else:
        print("1. SeqName [{0}]".format(user_sequence))
        for i in range(len(desc)):
            if names[i] == user_sequence:
                print("Description [{0}]".format(desc[i]))
        for i in range(len(seqs)):
            if names[i] == user_sequence:
                print("Sequence [{0}]".format(seqs[i]))
                seq_translation = translation(seqs[i])
                print("Translated Protein [{0}]".format(seq_translation))
                nuc_counts = nucleotide_counter1(seqs[i])
                for key, value in nuc_counts.items():
                    if key == 'A':
                        A_value = value
                    elif key == 'T':
                        T_value = value
                    elif key == 'G':
                        G_value = value
                    elif key == 'C':
                        C_value = value
                print("Nucleotide Counts: A=[{0}] T=[{1}] G=[{2}] C=[{3}]".format(A_value,T_value,G_value,C_value))
                GC_seq = gcContent(seqs[i])
                print("GC Content: {0}%".format(GC_seq))
                codons = get_codon1(seqs[i])
                print("Codon Profile:\n     Codon  Count")
                for key, values in codons.items():
                    print("     {0}    {1}".format(key, values))
        while True:
            user_restriction = input("Question 2: Which Restriction Enzyme to search? (e.g., GAATTC) ('q' for exit)")
            if user_restriction == 'q':
                break
            else:
                for i in range(len(seqs)):
                    if names[i] == user_sequence:
                        rest_match = enzymeFinder(user_restriction, seqs[i])
                        length = len(rest_match)
                        if length == 0:
                            print("Restriction Enzyme not found")
                        else:
                            print("There are {0} {1} restriction enzyme sites detected:".format(length, user_restriction))
                        for key, value in rest_match.items():
                            print("({0}) {1} Start Position [{2}] End Position [{3}]".format(key, user_restriction, value[0], value[1]))







