## Zadanie 1
```python
fh = open('sequences.fasta')
for line in fh:
    print(line)
fh.close()
```



## Zadanie 2
```python
fh = open('sequences.fasta')
for line in fh:
    for letter in line:
    	if letter == '>':
            print(line)
fh.close()
```

## Zadanie 3
```python
fh = open('sequences.fasta')
for line in fh:
    for letter in line:
        if letter == '>':
            index = line.find(' ')
            print((line.replace('>', ''))[:index])
fh.close()
```

## Zadanie 4
```python
fh = open('sequences.fasta')
for line in fh:
    for letter in line:
        if letter == '>':
            index = line.find(' ')
            line = line.replace('>', '')
            print("ID: ", line[:index], " ACCESSION: ", line[index:])
fh.close()
```

## Zadanie 5
```python
fh = open('sequences.fasta')
ids = []
for line in fh:
    for letter in line:
        if letter == '>':
            index = line.find(' ')
            line = (line.replace('>', ''))[:index]
            ids.append(line);
print(ids)
fh.close()
```

## Zadanie 6
```python
fh = open('human.txt')
plus = 0
for line in fh:
    if not line.startswith('#'):
        if " +" in line:
            plus += 1
print(plus)
fh.close()
```

## Zadanie 7
```python
fh = open('human.txt')
fh.readline()
plus = 0
for line in fh:
    if " +" in line:
        plus += 1
print(plus)
fh.close()
```

## Zadanie 8
```python
fh = open('human.txt')
fh.readline()
plus = 0
for line in fh:
    if " +" in line:
        plus += 1
percentage = plus/20*100
print(f'Genes (+): {percentage:.1f}%')
print(f'Genes (-): {(100-percentage):.1f}%')
fh.close()
```

## Zadanie 9
```python
fh = open('human.txt')
fh.readline()
genes = []      
for line in fh:
    columns = line.split()
    name = columns[0]
    start = int(columns[1])
    if start > 1000000:
        genes.append(name)

print(genes)
fh.close()
```

## Zadanie 10
```python
fh = open('human.txt')
fh.readline()
genes = []      
for line in fh:
    columns = line.split()
    name = columns[0]
    start = int(columns[1])
    end = int(columns[2])
    print("Gene ID:", name, " Length:", end-start, "bp")
    if start > 1000000:
        genes.append(name)

print(genes)
fh.close()
```

## Zadanie 11
```python
fh = open('human.txt')
fh.readline()
genes = []
lenghts = []      
for line in fh:
    columns = line.split()
    name = columns[0]
    start = int(columns[1])
    end = int(columns[2])
    lenghts.append(end-start)
    if start > 1000000:
        genes.append(name)
        
print(max(lenghts))
print(genes)
fh.close()
```

## Zadanie 12
```python
fh = open('human.txt')
fh.readline()
genes = []
gene = []      
for line in fh:
    columns = line.split()
    name = columns[0]
    start = int(columns[1])
    end = int(columns[2])
    gene.append(end-start)
    gene.append(name)
    genes.append(list (gene))
    gene.clear()

genes.sort(reverse = True)
print(genes[:3])
fh.close()
```

## Zadanie 17
```python
names = ['SAMD11', 'NOC2L', 'KLHL17']
names.sort()

oh = open('mygenes.txt', 'w')
for name in names:
    oh.write(f'{name}\n')
oh.close()
```

## Zadanie 18
```python
names = ['OR4F5', 'OR4F29', 'OR4F16', 'SAMD11', 'NOC2L']
values = [918, 939, 939, 20654, 15106]
listLength = len(names)
output = open('mygenes.txt', 'w')
for i in range(listLength):
	output.write(f'{names[i]}\t{values[i]}\n')
output.close()
```

## Zadanie 19
```python
names = ['OR4F5', 'OR4F29', 'OR4F16', 'SAMD11', 'NOC2L']
values = [918, 939, 939, 20654, 15106]
outputList = list(zip(values, names))
outputList.sort()
output = open('mygenes.txt', 'w')
for el1, el2 in outputList:
	output.write(f'{el1} {el2}\n')
output.close()
```

## Zadanie 20
```python
fh = open('human.txt')
fh.readline()
output = open('human_length.txt', 'w') 
for line in fh:
    columns = line.split()
    name = columns[0]
    start = int(columns[1])
    end = int(columns[2])
    output.write(f'{name}  {end-start}\n')
    
fh.close()
output.close()
```

## Zadanie 21
```python
fh = open('words_english.txt')
count = 0
for line in fh:
    if len(line) > 3:				
        line = line[:-1]			
        if line == line[::-1]:		
           count += 1

print(count)
fh.close()
```

## Zadanie 22
```python
fh = open('words_english.txt')
output = open('palindromes.txt', 'w') 
for line in fh:
    if len(line) > 3:
        newLine = line[:-1]
        if newLine == newLine[::-1]:
            output.write(f'{newLine}\n')

fh.close()
output.close()
```

## Zadanie 23
```python
fh = open('words_english.txt')
output = open('palindromes2.txt', 'w')
palindromes = [] 
for line in fh:
    if len(line) > 3:
        newLine = line[:-1]
        if newLine == newLine[::-1]:
            palindromes.append(newLine)

palindromes.sort(key = len, reverse = True)
for i in range(len(palindromes)):
    output.write(f'{palindromes[i]}\n')
fh.close()
output.close()
```

## Zadanie 24
```python
for i in range(1, 11):
    name = 'seq' + str(i) + '.genbank.txt'
    fh = open(name)
    for line in fh:
    	if line.startswith('ACCESSION'):
           ID = line.split()
           print(ID[1])
    fh.close()
```

## Zadanie 25
```python
for i in range(1, 11):
    name = 'seq' + str(i) + '.genbank.txt'
    fh = open(name)
    ID = ''
    percentage = 0
    sequence = ''
    for line in fh:
        if line.startswith('ACCESSION'):
           buff = line.split()
           ID = buff[1]
        if line.startswith('ORIGIN'):
            for line in fh:
            	for letter in line:
                    if letter == 'c' or letter == 'g' or letter == 'a' or letter == 't':
                    	sequence += letter
            percentage = (sequence.count('g') + sequence.count('c'))/len(sequence) * 100
            print(f'{ID} {percentage:.2f}')
    fh.close()
```