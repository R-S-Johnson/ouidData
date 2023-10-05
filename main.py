import matplotlib.pyplot as plt



with open("data.txt") as f:
    data = [line.split(',') for line in f.readlines()]

x = []
y = []
numTotal = 0

for i, day in enumerate(data):
    for dose in day:
        time, num = dose.split(':')
        numTotal += int(num)
        x.append(int(time))
        y.append(30 - i)

plt.plot(x, y, marker=".", linestyle='')
plt.show()
