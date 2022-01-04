'''
Problem 002
Transcribing DNA into RNA
Rosalind ID: RNA
'''

with open('/Users/anmoljandaur/Projects/ajandaur/Rosalind/RNA/rosalind_rna.txt', 'r') as infile:
    dna = ''.join(infile.read().strip())

rna = dna.replace('T', 'U')

with open('/Users/anmoljandaur/Projects/ajandaur/Rosalind/RNA/output_RNA.txt', 'w') as outfile:
    outfile.write(rna)