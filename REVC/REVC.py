'''
Problem 003
Complementing a Strand of DNA
Rosalind ID: REVC
'''

with open('/Users/anmoljandaur/Projects/ajandaur/Rosalind/REVC/rosalind_revc.txt', 'r') as infile:
    seq = ''.join(infile.read().strip())

    nucleo = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    revc = ''.join([nucleo[base] for base in reversed(seq)])

    with open('/Users/anmoljandaur/Projects/ajandaur/Rosalind/REVC/output_revc.txt', 'w') as outfile:
        outfile.write(revc)

