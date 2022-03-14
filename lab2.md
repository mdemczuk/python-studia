## Zadanie 8
```python
age = 23
if age >= 21:
    print("You are an adult, and so you should already have a job")
elif age > 18:
    print("You are not a minor anymore")
elif age > 16:
    print("You can drive a car")
elif age > 13:
    print("You can get ice cream")
elif age > 5:
    print("You can get candy")
else:
    print("You need a nap") 
```

## Zadanie 9
```python
name = input("Enter your name: ")
temp = float(input("Enter temperature in Celsius: "))
temp = (temp*(9/5)+32)
print(name)
print(temp)
```


## Zadanie 10
```python 
for letter in seq:
    if letter == "T":
        print(position)
    position = position + 1
```

## Zadanie 11
```python 
seq = input("Enter a DNA sequence: ")

for letter in seq:
    if letter == "T":
        print("A", end = "")
    elif letter == "A":
        print("T", end = "")
    elif letter == "G":
        print("C", end = "")
    elif letter == "C":
        print("G", end = "")
print()
```

## Zadanie 18
```python 
lst1 = ['a', 'b', 'c']
lst2 = []
for letter in lst1:
    lst2.append(letter*2)
print(lst1)
print(lst2)
```

## Zadanie 19
```python 
lst1 = ['a', 'b', 'c']
for i in range(len(lst1)):
    lst1[i] = lst1[i]*2
print(lst1)
```

## Zadanie 20
```python 
human = [2269, 542, 54, 21]
mouse = [881, 179, 12, 11]
Sum = []
x = 0
for i in human:
    Sum.append(human[x] + mouse[x])
    x += 1
```

## Zadanie 28
```python 
x = " ".join(counts).split()
for i in range(2, len(x), 3):
    print(x[i])
```

## Zadanie 29
```python 
lst = []
x = " ".join(counts).split()
for i in range(2, len(x), 3):
    print(x[i])
    z = int(x[i])
    #print(z)
    lst.append(z)

j = 0
for i in range(0, len(lst)):
    percentage = (lst[i])/1584224*100
    print(f'{x[j]}: {percentage:.1f}%')
    j += 3
```