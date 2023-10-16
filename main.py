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
        if len(time) < 3:
            time = int(time)/60*100
        else:
            time = int(time[-2:])/60*100 + int(time[:-2])*100
        if len(num) > 1 and num[1] != '\n':
            hit = num[1]
            num = num[0]
            if hit == 'g':
                xGas.append(time)
                yGas.append(30 - i)
        else:
            xCart.append(time)
            yCart.append(30 - i)
        numTotal += int(num)


plt.plot(xGas, yGas, marker=".", linestyle='', color="green")
plt.plot(xCart, yCart, marker='.', linestyle='', color='red')
plt.show()
