import math

# e to the power 2

x = 2
ePower = 0

for i in range(11):
    ePower += x ** i / math.factorial(i)

# print(ePower)

##############################################################################

# ln the natural log (2 >= x > 0)

x = 2

s = 0
for i in range(1, 1000):
    s += (-1) ** (i + 1) * (x - 1) ** i / i

# print(s)

#################################################################################

# ln the natural log (x > 0)

x = 2
k = 0
for i in range(-1, 1000, 2):
    k += 2 * ((1 / (i + 2)) * ((x - 1) / (x + 1)) ** (i + 2))

# print(k)

###############################################################################

# log the common log with base

y = 1
base = 10
t = 0
for i in range(1, 1000):
    t += (-1) ** (i + 1) * (x - 1) ** i / (i * math.log(base))

# print(t)

