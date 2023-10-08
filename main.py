import matplotlib.pyplot as plt



with open("data.txt") as f:
    data = [line.split(',') for line in f.readlines()]

xCart = []
yCart = []
xGas = []
yGas = []
numTotal = 0

for i, day in enumerate(data):
    for dose in day:
        time, num = dose.split(':')
        hit = None
        if len(num) > 1 and num[1] != '\n':
            hit = num[1]
            num = num[0]
        if hit != None and hit == 'g':
            xGas.append(int(time))
            yGas.append(30 - i)
        else:
            xCart.append(int(time))
            yCart.append(30 - i)
        numTotal += int(num)


plt.plot(xGas, yGas, marker=".", linestyle='', color="green")
plt.plot(xCart, yCart, marker='.', linestyle='', color='red')
plt.show()
