## Zadanie 22
```python
seq = 'CGAGCGCGGCGCCCTTGAGCTGCACCGCGGCGCAGGTTTGCGAGCCGACTTGTCAGCCGG'
seqlen = len(seq)
print("Sequence lenght:", seqlen, "nt")
percentage = ((seq.count('C') + seq.count('G'))/seqlen) * 100
print(f'GC content: {percentage:.1f}%')
```

## Zadanie 25
```python
chain_a = '''SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKM
FCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVV
RRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILT
IITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKG
EPHHELPPGSTKRALPNNT'''

#print(chain_a)
#print(chain_a.count('\n')+1)

chain_b = chain_a.replace('\n', '')
#print(chain_b)
#print(len(chain_b))

#print(chain_b[143:156])

#print(chain_b.find('NLRVEYLDDRN')+1)

#firstLine = chain_a.find('\n')
print(chain_a[:chain_a.find('\n')])
```

## Zadanie 26
```python
dna = """GGGCTTGTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCT
GTGGCACTGCTGCGCCTCTGCTGCGCCTCGGGTGTCTTTT
GCGGCGGTGGGTCGCCGCCGGGAGAAGCGTGAGGGGACAG
ATTTGTGACCGGCGCGGTTTTTGTCAGCTTACTCCGGCCA
AAAAAGAACTGCACCTCTGGAGCGG"""

rna = dna.replace('T', 'U').replace('\n', '')
#print(rna)
intron = rna[50:156]
#print(intron)
mrna1 = rna[:rna.find(intron)]
mrna2 = rna[(len(mrna1)+len(intron))-1:]
print(mrna1)
print(mrna2)
mrna = mrna1+mrna2
print(mrna)
```