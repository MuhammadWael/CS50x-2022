while True:
    try:
        x = float(input("Change owed:"))
    except ValueError:
        continue
    if x >= 0:
        break
x = x*100
quaters = 0
dimes = 0
nickels = 0
pennis = 0

while x >= 25:

    x -= 25
    quaters += 1

while x >= 10:

    x -= 10
    dimes += 1

while x >= 5:

    x -= 5
    nickels += 1

while x >= 1:

    x -= 1
    pennis += 1

print(quaters+dimes+nickels+pennis)