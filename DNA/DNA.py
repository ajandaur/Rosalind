'''
Problem 001
Counting DNA Nucleotides
Rosalind ID: DNA
'''

f = open("/Users/anmoljandaur/Developer/ajandaur/Rosalind/DNA/rosalind_data.txt",'r')
raw_data = f.readline().rstrip()
f.close()

print(raw_data.count('A'))
print(raw_data.count('C'))
print(raw_data.count('G'))
print(raw_data.count('T'))