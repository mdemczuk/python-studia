## Zadanie 2
```python
lst1 = [1, 2, 3]
lst2 = [3, 1, 4]
lst3 = [6, 2, 5]
lists = [lst1, lst2, lst3]
combinations = list(itertools.product(*lists))
import itertools
```

## Zadanie 14
```python
import urllib.request

uniprot_ids = ['P68431', 'Q6ZQ08', 'O94687']
output = open('uniprot.txt', 'w')

for id in uniprot_ids:
    f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{id}.fasta')
    for line in f:
        line = line.decode('utf-8')
        if not line.startswith('>'):
            output.write(line)

output.close()
```

## Zadanie 16
```python
import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True,
                    nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt',
                    help='Output filename (default: %(default)s)')
args = parser.parse_args()

fh = open(args.output, 'w')

f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{args.uniprot}.fasta')
for line in f:
    line = line.decode('utf-8')
    fh.write(line)

fh.close()
```

## Zadanie 17
```python
import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Retrieve proteins from UniProt database')
parser.add_argument('-i', '--id', dest='uniprot', required=True,
                    nargs='+', help='Uniprot ID (e.g. P68431)')
parser.add_argument('-o', '--o', '--out', dest='output', default='uniprot.txt',
                    help='Output filename (default: %(default)s)')
parser.add_argument('--format', dest='format', required=False, default='fasta',
                    help='File format (fasta/txt)')

args = parser.parse_args()

fh = open(args.output, 'w')

f = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{args.uniprot}.{args.format}')
for line in f:
    line = line.decode('utf-8')
    fh.write(line)

fh.close()
```