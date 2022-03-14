## Zadanie 1
```python
names = ['tnrc6a', 'PrP', 'bak1']
new_names = []

for i in range(0, len(names)):
	name = 'Hs' + names[i].upper()
	new_names.append(name)
```

## Zadanie 18
```python
fh = open('cancer1.txt')
skin_cancer = set(fh.read().split())
fh.close()

fh = open('cancer2.txt')
blood_cancer = set(fh.read().split())
fh.close()

fh = open('control.txt')
control = set(fh.read().split())
fh.close()

fh = open('cancer_common.txt', 'w')
cancer_common = list((skin_cancer & blood_cancer) - control)
for i in range(0, len(cancer_common)):
	fh.write(f'{cancer_common[i]}\n')
fh.close()
```

## Zadanie 19
```python
fh = open('cancer1.txt')
skin_cancer = set(fh.read().split())
fh.close()

fh = open('cancer2.txt')
blood_cancer = set(fh.read().split())
fh.close()

fh = open('control.txt')
control = set(fh.read().split())
fh.close()

fh = open('cancer_common.txt', 'w')
cancer_common = list((skin_cancer & blood_cancer) - control)
sorted_cancer_common = sorted(cancer_common)
for i in range(0, len(sorted_cancer_common)):
	fh.write(f'{sorted_cancer_common[i]}\n')
fh.close()

```