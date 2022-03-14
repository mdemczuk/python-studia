## Zadanie 1
```python
fh = open('Mycoplasma_hominis.fasta')

d = {}
key = ""

for line in fh:
	if line.startswith('>'):
		key = (line.lstrip('>')).split(' ')[0]
		d[key] = ""
	else:
		d[key] += line.rstrip()

fh.close()

fh = open('Mycoplasma_hominis.gtf')
output = open('genes.fasta', 'w')

for line in fh:
	if not line.startswith('#'):
		t = line.split('\t')
		if t[2] == 'gene':
			key = t[0]
			pos1 = int(t[3])
			pos2 = int(t[4])
			strand = t[6]
			gene_id = t[8]
			gene_id = ((gene_id.split(' ')[1]).lstrip('"')).rstrip('";')
			output.write(f'>{key}|gene|{gene_id}|{pos1}:{pos2}|{strand}\n{d[key][pos1-1:pos2]}\n')

fh.close()
output.close()
```

## Zadanie 2
```python
def complement(sequence):
	s = { 'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'
	}
	complementarySeq = ''
	for i in range(0, len(sequence)):
		complementarySeq += s[sequence[i]]
	return complementarySeq

def reverse_complement(sequence):
	return complement(sequence)[::-1]

fh = open('Mycoplasma_hominis.fasta')

d = {}
key = ""

for line in fh:
	if line.startswith('>'):
		key = (line.lstrip('>')).split(' ')[0]
		d[key] = ""
	else:
		d[key] += line.rstrip()

fh.close()

fh = open('Mycoplasma_hominis.gtf')
output = open('genes.fasta', 'w')

for line in fh:
	if not line.startswith('#'):
		t = line.split('\t')
		if t[2] == 'gene':
			key = t[0]
			pos1 = int(t[3])
			pos2 = int(t[4])
			strand = t[6]
			gene_id = t[8]
			gene_id = ((gene_id.split(' ')[1]).lstrip('"')).rstrip('";')
			if strand == '+':
				output.write(f'>{key}|gene|{gene_id}|{pos1}:{pos2}|{strand}\n{d[key][pos1-1:pos2]}\n')
			else:
				seq = d[key][pos1-1:pos2]
				seq = reverse_complement(seq)
				output.write(f'>{key}|gene|{gene_id}|{pos1}:{pos2}|{strand}\n{seq}\n')


fh.close()
output.close()
```

## Zadanie 3
```python
def complement(sequence):
	s = { 'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'
	}
	complementarySeq = ''
	for i in range(0, len(sequence)):
		complementarySeq += s[sequence[i]]
	return complementarySeq

def reverse_complement(sequence):
	return complement(sequence)[::-1]

def wrap(sequence, chars_per_line):
	text = ''
	for i in range(len(sequence)):
		if i % chars_per_line == 0 and i != 0:
			text += '\n'
		text += sequence[i]
	return text

fh = open('Mycoplasma_hominis.fasta')

d = {}
key = ""

for line in fh:
	if line.startswith('>'):
		key = (line.lstrip('>')).split(' ')[0]
		d[key] = ""
	else:
		d[key] += line.rstrip()

fh.close()

fh = open('Mycoplasma_hominis.gtf')
output = open('genes.fasta', 'w')

for line in fh:
	if not line.startswith('#'):
		t = line.split('\t')
		if t[2] == 'gene':
			key = t[0]
			pos1 = int(t[3])
			pos2 = int(t[4])
			strand = t[6]
			gene_id = t[8]
			gene_id = ((gene_id.split(' ')[1]).lstrip('"')).rstrip('";')
			seq = d[key][pos1-1:pos2]
			if strand == '-':
				seq = reverse_complement(seq)
			seq = wrap(seq, 50)
			output.write(f'>{key}|gene|{gene_id}|{pos1}:{pos2}|{strand}\n{seq}\n')


fh.close()
output.close()
```

## Zadanie 4
```python
import sys

args = sys.argv

def complement(sequence):
	s = { 'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'
	}
	complementarySeq = ''
	for i in range(0, len(sequence)):
		complementarySeq += s[sequence[i]]
	return complementarySeq

def reverse_complement(sequence):
	return complement(sequence)[::-1]

def wrap(sequence, chars_per_line):
	text = ''
	for i in range(len(sequence)):
		if i % chars_per_line == 0 and i != 0:
			text += '\n'
		text += sequence[i]
	return text

fh = open(args[1])

d = {}
key = ""

for line in fh:
	if line.startswith('>'):
		key = (line.lstrip('>')).split(' ')[0]
		d[key] = ""
	else:
		d[key] += line.rstrip()

fh.close()

fh = open(args[2])
output = open('genes.fasta', 'w')

for line in fh:
	if not line.startswith('#'):
		t = line.split('\t')
		if t[2] == 'gene':
			key = t[0]
			pos1 = int(t[3])
			pos2 = int(t[4])
			strand = t[6]
			gene_id = t[8]
			gene_id = ((gene_id.split(' ')[1]).lstrip('"')).rstrip('";')
			seq = d[key][pos1-1:pos2]
			if strand == '-':
				seq = reverse_complement(seq)
			seq = wrap(seq, 50)
			output.write(f'>{key}|gene|{gene_id}|{pos1}:{pos2}|{strand}\n{seq}\n')


fh.close()
output.close()
```

## Zadanie 5
```python
import sys

args = sys.argv

def complement(sequence):
	s = { 'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'
	}
	complementarySeq = ''
	for i in range(0, len(sequence)):
		complementarySeq += s[sequence[i]]
	return complementarySeq

def reverse_complement(sequence):
	return complement(sequence)[::-1]

def wrap(sequence, chars_per_line):
	text = ''
	for i in range(len(sequence)):
		if i % chars_per_line == 0 and i != 0:
			text += '\n'
		text += sequence[i]
	return text

fh = open(args[1])

d = {}
key = ""

for line in fh:
	if line.startswith('>'):
		key = (line.lstrip('>')).split(' ')[0]
		d[key] = ""
	else:
		d[key] += line.rstrip()

fh.close()

fh = open(args[2])
output = open('genes.fasta', 'w')

for line in fh:
	if not line.startswith('#'):
		t = line.split('\t')
		if t[2] == args[3]:
			key = t[0]
			pos1 = int(t[3])
			pos2 = int(t[4])
			strand = t[6]
			gene_id = t[8]
			gene_id = ((gene_id.split(' ')[1]).lstrip('"')).rstrip('";')
			seq = d[key][pos1-1:pos2]
			if strand == '-':
				seq = reverse_complement(seq)
			seq = wrap(seq, 50)
			output.write(f'>{key}|{args[3]}|{gene_id}|{pos1}:{pos2}|{strand}\n{seq}\n')


fh.close()
output.close()
```