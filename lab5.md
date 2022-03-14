## Zadanie 2
```python
def gc_content(str):
    c_count = str.count('C') 
    g_count = str.count('G') 
    result = (c_count + g_count) / len(str)
    print(f"CG content is {result}")

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

gc_content(dna)
```

## Zadanie 4
```python
def gc_content(str):
    c_count = str.count('C') 
    g_count = str.count('G') 
    return (c_count + g_count) / len(str)

gc = gc_content(str = 'ATGC')
print(gc)
print(gc_content('ATGC'))
```

## Zadanie 6
```python
def hamming_distance(str1, str2):
    result = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            result += 1
    return result

seq1 = "GAGCCTACTAACGGGAT"
seq2 = "CATCGTAATGACGGCCT"

print(hamming_distance(seq1, seq2))
```

## Zadanie 7
```python
def hamming_distance(str1, str2):
    result = 0
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            result += 1
    return result

print(hamming_distance('ACTG', 'actg'))
```

## Zadanie 14
```python
def hamming_distance(str1, str2):
    """A function that counts the number of positions in which two strings are different.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        int: The return value is the Hamming distance. 

    """
    result = 0
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            result += 1
    return result

help(hamming_distance)
print(hamming_distance.__doc__)
```

## Zadanie 15
```python
def complement(sequence):
    d = { 'A': 'T',
          'T': 'A',
          'G': 'C',
          'C': 'G'
    }
    complementarySeq = ''
    for i in range(0, len(sequence)):
        complementarySeq += d[sequence[i]]
    return complementarySeq

print(complement('ACTG'))
```

## Zadanie 16
```python
def complement(sequence):
    d = { 'A': 'T',
          'T': 'A',
          'G': 'C',
          'C': 'G'
    }
    complementarySeq = ''
    for i in range(0, len(sequence)):
        complementarySeq += d[sequence[i]]
    return complementarySeq

def reverse_complement(sequence):
    return complement(sequence)[::-1]

print(reverse_complement('ACTG'))
```

## Zadanie 17
```python
def complement(sequence):
    d = { 'A': 'T',
          'T': 'A',
          'G': 'C',
          'C': 'G'
    }
    complementarySeq = ''
    for i in range(0, len(sequence)):
        complementarySeq += d[sequence[i]]
    return complementarySeq

def reverse_complement(sequence):
    return complement(sequence)[::-1]

lst = ['CTGACT', 'GCATAGT', 'TAGATTAT', 'CGATGTTTA']
for i in range(0, len(lst)):
    print(reverse_complement(lst[i]))
```

## Zadanie 20
```python
def mutate(sequence):
    import random
    postition = random.randint(0, len(sequence)-1)
    substitution = random.choice(['A', 'T', 'G', 'C'])
    print(sequence.replace(sequence[postition], substitution, 1))

mutate('ATGCG')
```