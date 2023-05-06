# a
full = False
counter = 100
MAX = 200

if not full and counter < MAX:
    counter += 3
else:
    counter = 0

# b
for i in range(10, -1, -2):
    print(i)

# c
values = [-20, 10, 34, -4, 44]
pos = []
neg = []

for value in values:
    if value < 0:
        neg.append(value)
    else:
        pos.append(value)

print(pos, neg)

# d
values = [5, 24, 33, 8, 9, 15]
total = 0
threshold = 50

for value in values:
    if total > threshold:
        break
    total += value
print(total)

total = 0

index = 0
while total <= threshold and index < len(values):
    total += values[index]
    index += 1
print(total)

