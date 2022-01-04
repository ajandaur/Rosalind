"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content,
followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless
otherwise stated; please see the note on absolute error below.
"""


# read the file
def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


FASTAFile = readFile('/Users/anmoljandaur/Developer/ajandaur/Rosalind/GC/rosalind_gc.txt')

FASTADict = {}

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

MAXGCKey = max(RESULTDict, key=RESULTDict.get)

print(f'{MAXGCKey[1:]}\n{RESULTDict[MAXGCKey]}')
