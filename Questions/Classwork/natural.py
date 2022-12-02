end = 5
total = 0
while end > 0:
    total = total + end
    end = end - 1

print(total)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue

    print(i)

