## Zadanie 11
```python
d = {
    'alpha': [1, 2, 3],
    'beta': 'bioinfo',
    'gamma': 4,
    'delta': {'key': 'val'}
}

print(d['alpha'])

d['alpha'].append(4)

print(d['alpha'][3])

print(d['beta'][0])

print(d['delta']['key'])
```

## Zadanie 12
```python
d = {}
l = [
  'gene1   54      3234',
  'gene2   6031    100321',
  'gene3   12381   142132'
]
buff = []
for el in l:
    buff = el.split()
    d[buff[0]] = []
    d[buff[0]].append(buff[1])
    d[buff[0]].append(buff[2])
    buff.clear()

print(d)
```

## Zadanie 13
```python
protein_weights = { 
   'A': 89.0932, 
   'C': 121.1582, 
   'D': 133.1027, 
   'E': 147.1293, 
   'F': 165.1891, 
   'G': 75.0666, 
   'H': 155.1546, 
   'I': 131.1729, 
   'K': 146.1876, 
   'L': 131.1729, 
   'M': 149.2113, 
   'N': 132.1179, 
   'O': 255.3134, 
   'P': 115.1305, 
   'Q': 146.1445, 
   'R': 174.201, 
   'S': 105.0926, 
   'T': 119.1192, 
   'U': 168.0532, 
   'V': 117.1463, 
   'W': 204.2252, 
   'Y': 181.1885 
}

pep = "MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNXCEVVLGNLEITYVQRNYDLSFLKTXIQEVAGYVL"

weight = 0
for el in range(0, len(pep)):
    if pep[el] != 'X':
        weight += protein_weights[pep[el]]

print(weight)
```

## Zadanie 14
```python
complementary_seq = {
	'A': 'T',
	'T': 'A',
	'G': 'C',
	'C': 'G'
}

dna = 'AGCCCGATGCTTA'
cdna = ''

for i in range(0, len(dna)):
    cdna += complementary_seq[dna[i]]

print(cdna)
```

## Zadanie 16
```python
seq = 'MNNGGKAEKENTPSEANLQEEEVRTLFVSGLPLDIKPRELYLLFRPFKGYEGSLIKLTSKQPVGFVSFDSRSEAEAAKNALNGIRFDPEI'

d = {}
for char in seq:
    if char not in d:
        d[char] = 0
    d[char] += 1

output = open('output.txt', 'w')
output.write(f'#aa\tpercent\n')
for key in d:
    percentage = d[key] / len(seq) * 100
    output.write(f'{key}\t{percentage:.1f}\n')
output.close()
```

## Zadanie 17
```python
dna = 'AGCCCGATGCTTAAACGTAGATTTTCC'

d = {}
count = 0
buff = ''
j = 0
for i in range(0, len(dna)-1):
    j = i
    while count < 2:
        buff += dna[j]
        count += 1
        j += 1
    
    if count == 2:
        if buff not in d:
            d[buff] = 0
        d[buff] += 1
        count = 0
        buff = ''

sorted_d = sorted(d.items())
for i, j in sorted_d:
    print(i, j)
```

## Zadanie 18
```python
d = {}

fh = open('ecoli.pep.fasta')

key = ""

for line in fh:
    if line.startswith(">"):
        key = line.split(' ')[0]
        continue
    if key not in d.keys():
        d[key] = ""
    d[key] += line.rstrip()
    
print(d)
```

## Zadanie 19
```python
d = {}
protein_weights = { 
   'A': 89.0932, 
   'C': 121.1582, 
   'D': 133.1027, 
   'E': 147.1293, 
   'F': 165.1891, 
   'G': 75.0666, 
   'H': 155.1546, 
   'I': 131.1729, 
   'K': 146.1876, 
   'L': 131.1729, 
   'M': 149.2113, 
   'N': 132.1179, 
   'O': 255.3134, 
   'P': 115.1305, 
   'Q': 146.1445, 
   'R': 174.201, 
   'S': 105.0926, 
   'T': 119.1192, 
   'U': 168.0532, 
   'V': 117.1463, 
   'W': 204.2252, 
   'Y': 181.1885 
}

fh = open('ecoli.pep.fasta')

key = ""
weight = 0
for line in fh:
    if line.startswith(">"):
        key = line.split(' ')[0]
        weight = 0
        continue
    else:
        for letter in line:
            if letter in protein_weights.keys():
                weight += protein_weights[letter]
    if key not in d.keys():
        d[key] = ""
    d[key] = weight

fh.close()
output = open('ecoli.mass.txt', 'w')

for key in d:
    output.write(f'{key}\t{d[key]:.1f}\n')

output.close()
```

## Zadanie 20
```python
d = {}

fh = open('lotto_history.txt')

key = 0
buff = ""
for line in fh:
    buff += (line.split(' ')[2])

fh.close()

buff = (buff.replace("\n", ",")).split(",")
for i in range(0, len(buff)):
    key = int(buff[i])
    buff[i] = int(buff[i])
    if key not in d.keys():
        d[key] = 0

for key in d:
    d[key] = buff.count(key)

sorted_by_values = sorted(d, key=d.get, reverse = True)
for i in range(0, 10):
    print(f'Number: {sorted_by_values[i]}, number of occurrences: {d[sorted_by_values[i]]}')
```