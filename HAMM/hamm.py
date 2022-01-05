"""
Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

"""

with open('/Users/anmoljandaur/Developer/ajandaur/rosalind_challenges/REVC/rosalind_hamm.txt', 'r') as data:
    data_set = data.read().splitlines()

    # first DNA string
    firstDNA = data_set[0]
    # second DNA string
    secondDNA = data_set[1]

    pointCount = 0

    for n in range(len(firstDNA)):
        if firstDNA[n] != secondDNA[n]:
            pointCount += 1

print("# of point mutations is", pointCount)
